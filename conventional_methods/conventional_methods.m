close all; clear all; clc;

frame_based=true;
if (frame_based==true)
    text4input=["For BBC Learning English Video Words in the News Forest fires hit the US                           enter 1 ",...
        "For Dramatic evacuations by sea as forest fires rage in Italy and Turkey                           enter 2 ",...
        "For Drone footage shows before and after wildfires ravage Turkey's pine forests                    enter 3 ",...
        "For Drones vs. California's wildfires_ How they're helping firefighters                            enter 4 ",...
        "For Incredible Aerial Footage Shows New California Wildfire Burning in LA                          enter 5 ",...
        "For Raw Video Black Forest Fire                                                                    enter 6 ", ...
        "For Silviculture Surveying with UAVs in Forest Management                                          enter 7 ", ...
        "For Sunday Journal_ Apocalyptic Western wildfires                                                  enter 8 ", ...
        "For Turkey wildfires Drone footage shows destruction left by blaze                                 enter 9 ", ...
        "For US wildfires_ Firefighters continue battle against blazes that have left at least 35 dead      enter 10",...
        "For dalma_400240                                                                                   enter 11 ",...
        "For gwanak_400240                                                                                  enter 12 ",...
        "For nofire_400240                                                                                  enter 13 ",...
        "Enter your choice: "];
    text4input= strjoin(text4input, '\n');

    switch input(text4input)
        case 1
            imageDir = 'databases/BBC_Learning_English_Video_Words_in_the_News_Forest_fires_hit_the_US';
        case 2
            imageDir = 'databases/Dramatic_evacuations_by_sea_as_forest_fires_rage_in_Italy_and_Turkey';
        case 3
            imageDir = 'databases/Drone_footage_shows_before_and_after_wildfires_ravage_Turkeys_pine_forests';
        case 4
            imageDir = 'databases/Drones_vs._Californias_wildfires__How_theyre_helping_firefighters';
        case 5
            imageDir = 'databases/Incredible_Aerial_Footage_Shows_New_California_Wildfire_Burning_in_LA';
        case 6
            imageDir = 'databases/Raw_Video_Black_Forest_Fire';
        case 7
            imageDir = 'databases/Silviculture_Surveying_with_UAVs_in_Forest_Management';
        case 8
            imageDir = 'databases/Sunday_Journal__Apocalyptic_Western_wildfire';
        case 9
            imageDir = 'databases/Turkey_wildfires_Drone_footage_shows_destruction_left_by_blaze';
        case 10
            imageDir = 'databases/US_wildfires__Firefighters_continue_battle_against_blazes_that_have_left_at_least_35_dead';
        case 11
            imageDir = 'databases/dalma_400240';
        case 12
            imageDir = 'databases/gwanak_400240';
        case 13
            imageDir = 'databases/nofire_400240';
        otherwise
            disp("Please select one of the listed options!");
            return;
    end
else
    % This theoretically works, untested! -- acc works hahahahahhahah
    disp("Please drag and drop your video in the /videos_of_wildfire/ folder and press any key.");
    pause;
    database_generation_script;

    frame_folders = dir('databases/*');
    frame_folders = frame_folders([frame_folders.isdir]); 

    if isempty(frame_folders)
        error("No frame folders found in 'databases'. Please check the video processing.");
    end

    [~, idx] = max([frame_folders.datenum]);
    imageDir = fullfile('databases/', frame_folders(idx).name);
end

disp(['Loading frames from: ', imageDir]);
if ~isfolder(imageDir)
    error('The specified directory does not exist: %s', imageDir);
end

frame_files = dir(fullfile(imageDir, '*.jpg'));
if isempty(frame_files)
    error('No .jpg files found in the directory: %s', imageDir);
end
frame_struct = struct('name', [], 'data', [], 'size', []);
[~, sorted_idx] = sort({frame_files.name});
frame_files = frame_files(sorted_idx);

for k = 1:length(frame_files)
    filePath = fullfile(imageDir, frame_files(k).name);
    img = imread(filePath);
    
    frame_struct(k).name = frame_files(k).name;
    frame_struct(k).data = img;
    frame_struct(k).size = size(img); 
    figure(1);clf;
    imshow(frame_struct(k).data);
    title(frame_struct(k).name);
end 

clc;disp("Done! Total number of detected fire frames are: fuck all")
 
function cielab_image = frame_manipulation(video_frame,reference)
    % frame manipulation strategy

    if reference==0
        % it's reference, no subtracting
        subtracted=video_frame;
    else
        subtracted=video_frame-reference;
    end
    threshold=subtracted;

    cielab_image=rgb2lab(threshold);
    % do i really need to threshold? it appears perfect for edge detection
    % binarised=cielab_image(:,:,1);

    % 4. threshold the image
    % 5. do image processing and edge detection (look-up LR)
    % 6. binarise
end

% function classification_and_plotting(manipulated_image, original)
%     figure; subplot(1,2,1);imshow(manipulated_image);title("CIELAB");subplot(1,2,2);imshow(original);title("Original");
% 
%     % % classify the image
%     % 1. is a fire present? 
%     %     1.1 if yes then construct plot function for the area in a red box
%     %     1.2 if not then ignore
%     % 
%     % % plotting
%     % 1. plot the original
%     % 2. plot the fire area plot function
% end



