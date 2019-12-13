import os, pyautogui, PIL, shutil

def get_value(name, min, max, default):
    #TODO add min/max validation
    value = input("Enter " + name + " [" + str(default) + "]: ")
    if len(value) == 0:
        value = default
    return int(value)

def get_screen_area(resolution):    
    x = get_value("x", 0, resolution.width, 0)
    y = get_value("y", 0, resolution.height, 0)
    width = get_value("width", 0, resolution.width, resolution.width)
    height = get_value("height", 0, resolution.height, resolution.height)
    
    return {"x": x, "y": y, "width": width,"height": height}

def prepare_image(scrn, rectangle):
    start_x = rectangle["x"]
    start_y = rectangle["y"]
    max_x = rectangle["width"] - start_x
    max_y = rectangle["height"]  - start_y

    img = PIL.Image.new("RGB",(max_x, max_y))    
    pixels = img.load()
    for x in range(max_x):
        for y in range(max_y):
            pixels[x,y] = scrn.getpixel((x + start_x,y + start_y))

    return img

def analyze_img(img):
    #TODO
    pass

def save_image_to_disk(img):
    d = os.path.join(os.path.dirname(os.path.realpath(__file__)),"tmp")
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(d)
    file_path = os.path.join(d, "file.jpeg")
    img.save(file_path)

if __name__ == "__main__":
    #intro
    resolution = pyautogui.size()
    print("Your resolution",resolution)

    #screen area
    rect = get_screen_area(resolution)

    #minimize all windows
    pyautogui.hotkey('winleft', 'm')

    #screenshot
    scrn = pyautogui.screenshot()

    #create image
    img = prepare_image(scrn, rect)

    #analyze
    analyze_img(img)

    #save to disk
    save_image_to_disk(img)
    
    #show image
    img.show()
