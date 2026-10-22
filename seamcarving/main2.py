import cv2
import numpy as np

def read_image(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not read the image.")
        exit()

    n, m = image.shape[:2]

    if n < 2 or m < 2:
        print("Error: Image must have at least 2x2 pixels.")
        exit()
    
    print(f"Image size: {n}x{m}")

    return image

def calculate_energy(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Convert the image to float64
    gray = gray.astype(np.float64)

    # Calculate the gradient of the image
    dy, dx = np.gradient(gray)

    # Calculate the energy of the image
    energy = np.abs(dx) + np.abs(dy)

    return energy

def find_vertical_seam(energy):
    n, m = energy.shape

    dp = np.zeros((n, m), dtype=np.float64)
    father = np.zeros((n, m), dtype=np.int32)

    dp[0] = energy[0]

    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i, j] = energy[i, j] + min(dp[i - 1, j], dp[i - 1, j + 1])
                father[i, j] = j + np.argmin([dp[i - 1, j], dp[i - 1, j + 1]])
            elif j == m - 1:
                dp[i, j] = energy[i, j] + min(dp[i - 1, j - 1], dp[i - 1, j])
                father[i, j] = j - 1 + np.argmin([dp[i - 1, j - 1], dp[i - 1, j]])
            else:
                dp[i, j] = energy[i, j] + min(dp[i - 1, j - 1], dp[i - 1, j], dp[i - 1, j + 1])
                father[i, j] = j - 1 + np.argmin([dp[i - 1, j - 1], dp[i - 1, j], dp[i - 1, j + 1]])

    seam = np.zeros(n, dtype=np.int32)
    seam[n - 1] = np.argmin(dp[-1])

    for i in range(n - 2, -1, -1):
        seam[i] = father[i + 1, seam[i + 1]]
    
    return seam

def remove_vertical_seam(image, seam):
    n, m = image.shape[:2]

    mask = np.ones((n, m), dtype=bool)

    for i in range(n):
        mask[i, seam[i]] = False
    
    new_image = image[mask].reshape(
        n,
        m - 1,
        image.shape[2]
    )

    return new_image

def seam_carving_width(image, target_width):
    n, m = image.shape[:2]

    if target_width < m:
        print("Error: Target width not valid.")
        exit()

    while m < target_width:
        # Add at most half of the current width per round to avoid stretching the same region repeatedly
        k = min(target_width - m, m // 2)

        # Remove k seams from a copy, recording which original columns they come from
        temp = image
        index = np.tile(np.arange(m, dtype=np.int32), (n, 1))
        seams = np.zeros((k, n), dtype=np.int32)

        for t in range(k):
            energy = calculate_energy(temp)
            seam = find_vertical_seam(energy)
            seams[t] = index[np.arange(n), seam]
            temp = remove_vertical_seam(temp, seam)
            index = remove_vertical_seam(index[:, :, np.newaxis], seam)[:, :, 0]

        # Duplicate these seams in the original image, the new pixel is the average of the seam pixel and its right neighbor
        new_image = np.zeros((n, m + k, image.shape[2]), dtype=image.dtype)

        for i in range(n):
            row = image[i].astype(np.float64)
            cols = np.sort(seams[:, i])
            right = np.minimum(cols + 1, m - 1)
            values = (row[cols] + row[right]) / 2
            new_image[i] = np.insert(row, cols + 1, values, axis=0)

        image = new_image
        m += k
        print(f"Current width: {m}")

    return image

def write_image(image, output_path):
    cv2.imwrite(output_path, image)

if __name__ == "__main__":
    image = read_image("1.jpg")
    print("Image read successfully.")
    image = seam_carving_width(image, 1500)
    print("Image resized successfully.")
    write_image(image, "output.jpg")
    print("Image written successfully.")