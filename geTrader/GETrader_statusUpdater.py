import pyautogui as gui
import time as t
import cv2
import numpy as np

#Confience level
confidenceLevel = 0.9

def updateStatus():
    # Dictionary of images and corresponding statuses
    imageStatusMap = {
        "screenshots/wait.png": "Wait",
        "screenshots/abortOffer.png": "Abort Offer",
        "screenshots/collectItems.png": "Collect Items",
        "screenshots/buy.png": "Buy",
        "screenshots/sell.png": "Sell",
        # Add more images and their statuses as needed
    }

    for image, status in imageStatusMap.items():
        try:
            # Check if the image is on the screen
            if gui.locateOnScreen(image, confidence=confidenceLevel):
                print(f"Status updated to: {status}")
                return status  # Exit once an image is found
        except gui.ImageNotFoundException:
            # This will catch image not found exceptions and continue
            pass

    print("No images found.")
    return "No Status Found"

def abortOfferMethod():
    # Take a screenshot of the specified region
    gui.screenshot("screenshots/geRedBox.PNG", region=(475, 127, 475, 300))

    # Load the screenshot
    image = cv2.imread('screenshots/geRedBox.PNG')

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for the red color in HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for red color
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    # Find contours in the mask
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the top-left corner of the screenshot's region for offset adjustment
    region_top_left = (475, 127)

    # Draw rectangles and click on the center of each detected red box
    for contour in contours:
        # Get bounding box for the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Filter by size (optional, based on the box dimensions in the GE)
        if w > 20 and h > 20:  # Example dimensions

            # Calculate the center of the box
            center_x = x + w // 2
            center_y = y + h // 2

            # Adjust the center to the screen coordinates
            screen_center_x = center_x + region_top_left[0]
            screen_center_y = center_y + region_top_left[1]

            # Perform a click at the center of the box
            gui.click(screen_center_x, screen_center_y)

def sellMethod():
    # Take a screenshot of the inventory region
    gui.screenshot("screenshots/inventoryBox.png",
                   region=(1170, 427, 202, 273))  # Adjust `region` to your inventory coordinates
    # Adjust `region` to your inventory coordinates

    # Load the screenshot
    image = cv2.imread('screenshots/inventoryBox.png')

    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for the blue color in HSV
    lower_blue = np.array([100, 150, 50])  # Adjust based on your blue highlight color
    upper_blue = np.array([140, 255, 255])

    # Create a mask for the blue color
    blue_mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # Find contours in the mask
    contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get the top-left corner of the inventory region for offset adjustment
    region_top_left = (1170, 427)  # Adjust to match the `region` parameter in pyautogui.screenshot()

    # Draw rectangles and click on the center of each detected blue-highlighted item
    for contour in contours:
        # Get bounding box for the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Filter by size (to avoid small artifacts or noise)
        if w > 20 and h > 20:  # Adjust dimensions as needed
            # Draw the rectangle on the image (for debugging purposes)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Calculate the center of the box
            center_x = x + w // 2
            center_y = y + h // 2

            # Adjust the center to the screen coordinates
            screen_center_x = center_x + region_top_left[0]
            screen_center_y = center_y + region_top_left[1]

            # Perform a click at the center of the box
            gui.click(screen_center_x, screen_center_y)

def priceQuantityMethod():
    t.sleep(2)
    gui.click(669, 323) # Clicks Item Quantity
    t.sleep(2)
    gui.press("e")
    t.sleep(2)
    gui.press("Enter")
    t.sleep(2)
    gui.click(839, 321) # Clicks Item Price
    t.sleep(2)
    gui.press("e")
    t.sleep(2)
    gui.press("Enter")
    t.sleep(2)
    gui.click(713, 396) # Clicks Confirm
    t.sleep(2)

# Wait Done
def wait():
    print("Waiting...")
    t.sleep(5)
# Abort Offer Done
def abortOffer():
    print("Aborting Offer...")
    abortOfferMethod()
    t.sleep(2)
    gui.click(814, 382)
    t.sleep(2)
    gui.click(506, 398)
    t.sleep(2)
    print("Offer Aborted")
# Collect Items Done
def collectItems():
    print("Collecting Items...")
    gui.click(893, 178)
    print("Items Collected")
# Buy Done
def buy():
    print("Buying...")
    gui.click(gui.locateCenterOnScreen("screenshots/buyButton.png", confidence=confidenceLevel)) #Click Buy Button
    t.sleep(2)
    gui.click(527, 579) # Clicks Suggested Item
    priceQuantityMethod()
    print("Item Bought!")
# Sell Donee
def sell():
    print("Selling...")
    sellMethod()
    priceQuantityMethod()
    print("Item Sold!")
def main():
    status = updateStatus()
    if status == "Wait":
        wait()
    elif status == "Abort Offer":
        abortOffer()
    elif status == "Collect Items":
        collectItems()
    elif status == "Buy":
        buy()
    elif status == "Sell":
        sell()

loop = 8

while loop > 0:
    main()
    loop -= 1
    t.sleep(1)
