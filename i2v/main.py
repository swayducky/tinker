import re
import cv2
import os

def images_to_video(image_dir, video_name, fps):
    # Get a list of image files in the directory
    image_files = sorted(os.listdir(image_dir))
    
    # Read the first image to get the frame size
    frame = cv2.imread(os.path.join(image_dir, image_files[0]))
    height, width, _ = frame.shape

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # FourCC code for MP4
    video_writer = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    # Write each image frame to the video
    for image_file in image_files:
        frame = cv2.imread(os.path.join(image_dir, image_file))
        video_writer.write(frame)

    # Release the VideoWriter object
    video_writer.release()

    print(f'Video saved as {video_name}')


def image_to_video(image_path, video_name, fps, duration):
    # Read the image
    frame = cv2.imread(image_path)
    
    # Check if the image was read successfully
    if frame is None:
        print(f'Error: Unable to read image from {image_path}')
        return

    height, width, _ = frame.shape

    # Calculate the total number of frames based on the desired duration and fps
    total_frames = int(fps * duration)

    # Create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # FourCC code for MP4
    video_writer = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    # Write the image frame to the video repeatedly
    for i in range(total_frames):
        video_writer.write(frame)

    # Release the VideoWriter object
    video_writer.release()

    print(f'Video saved as {video_name}')

IMG_DIR = '_in_i2v/'

# images_to_video(IMG_DIR, '_out/i2v.mp4', 30)
# images_to_video(IMG_DIR, '_out/i2v.mp4', 30)

RX = re.compile(r'^.*\.(jpg|png|jpeg)$', re.IGNORECASE)
image_file = [f for f in os.listdir(IMG_DIR) if RX.match(f)][0]
image_path = os.path.join(IMG_DIR, image_file)
image_to_video(image_path, '_out/i2v.mp4', 1, 10)
