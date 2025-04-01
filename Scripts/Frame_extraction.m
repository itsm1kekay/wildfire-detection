clc; clear; close all;

input_folder = 'videos_of_wildfires'; 
output_folder = 'databases'; 

if ~exist(output_folder, 'dir')
    mkdir(output_folder);
end

video_files = dir(fullfile(input_folder, '*.mp4'));

if isempty(video_files)
    disp('No video files found in the input folder.');
else
    for i = 1:length(video_files)
        video_name = video_files(i).name;
        video_path = fullfile(input_folder, video_name);

        video_reader = VideoReader(video_path);

        [~, name, ~] = fileparts(video_name); 
        frame_folder = fullfile(output_folder, name);

        if exist(frame_folder, 'dir')
            disp(['Skipping ', video_name, ' (already processed).']);
            continue; 
        end

        mkdir(frame_folder);

        frame_idx = 1;
        while hasFrame(video_reader)
            frame = readFrame(video_reader);

            frame_filename = fullfile(frame_folder, sprintf('frame_%04d.jpg', frame_idx));
            imwrite(frame, frame_filename, 'Quality', 85);

            frame_idx = frame_idx + 1;
        end

        disp(['Finished processing: ', video_name, ' -> Frames saved in ', frame_folder]);
    end

    disp('All videos processed successfully!');
end
