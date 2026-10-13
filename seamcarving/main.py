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

    if target_width < 1 or target_width > m:
        print("Error: Target width not valid.")
        exit()

    while m > target_width:
        energy = calculate_energy(image)
        seam = find_vertical_seam(energy)
        image = remove_vertical_seam(image, seam)
        m -= 1
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