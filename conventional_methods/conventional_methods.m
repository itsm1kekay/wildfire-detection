close all; clear all; clc;





frame_based=false;

% frame extraction
if (frame_based==false)
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
    desired_video = input(text4input);

    switch desired_video
        case 1
            selected_video="videos_of_wildfires/BBC_Learning_English_Video_Words_in_the_News_Forest_fires_hit_the_US.mp4";
        case 2
            selected_video="videos_of_wildfires/Dramatic_evacuations_by_sea_as_forest_fires_rage_in_Italy_and_Turkey.mp4";
        case 3
            selected_video="videos_of_wildfires/Drone_footage_shows_before_and_after_wildfires_ravage_Turkeys_pine_forests.mp4";
        case 4
            selected_video="videos_of_wildfires/Drones_vs._Californias_wildfires__How_theyre_helping_firefighters.mp4";
        case 5
            selected_video="videos_of_wildfires/Incredible_Aerial_Footage_Shows_New_California_Wildfire_Burning_in_LA.mp4";
        case 6  
            selected_video="videos_of_wildfires/Raw_Video_Black_Forest_Fire.mp4";
        case 7
            selected_video="videos_of_wildfires/Silviculture_Surveying_with_UAVs_in_Forest_Management.mp4";
        case 8
            selected_video="videos_of_wildfires/Sunday_Journal__Apocalyptic_Western_wildfire.mp4";
        case 9
            selected_video="videos_of_wildfires/Turkey_wildfires_Drone_footage_shows_destruction_left_by_blaze.mp4";
        case 10
            selected_video="videos_of_wildfires/US_wildfires__Firefighters_continue_battle_against_blazes_that_have_left_at_least_35_dead.mp4";
        case 11
            selected_video="videos_of_wildfires/dalma_400240.mp4";
        case 12
            selected_video="videos_of_wildfires/gwanak_400240.mp4";
        case 13
            selected_video="videos_of_wildfires/nofire_400240.mp4";
        otherwise
            disp("Please select one of the listed options!");
            return;
            
    end
    clc;    disp("Please wait, processing...")
    video_frames= frame_extraction(selected_video);
    [~,name,~]=fileparts(selected_video);
    save(name,"video_frames","-v7.3");
end
for i=2:size(video_frames,4)
    video_frame_i = video_frames(:,:,:,i);
    video_frame_1_previous=video_frames(:,:,:,i-1);

    % frame manipulation
    manipulated_image_i=frame_manipulation(video_frame_i,video_frame_1_previous);

    % classification and plotting
    if i == 100
        figure; 
        subplot(1,2,1);imshow(manipulated_image_i); title("Frame 10 CIELAB");
        subplot(1,2,2);imshow(video_frame_i); title("Original frame 10")
    end
end
clc;disp("Done")

function video_frames= frame_extraction(input)
    imported_video=VideoReader(input);
    num_of_frames=floor(imported_video.Duration*imported_video.FrameRate);
    frame_array=zeros(imported_video.Height,imported_video.Width,3, ...    
        num_of_frames,'uint8');                                             % 'uint8' for 8 bit video (24 for rgb)
    frame_index=1;                                                          % 'uint16' for 16 bit video (48 for rgb)
    while hasFrame(imported_video)
        frame_array(:,:,:,frame_index)=readFrame(imported_video);
        frame_index= frame_index+1;
    end
    video_frames=frame_array;
    % video_frames = frame_array(:, :, :, 1:frame_index-1);                 % truncate to accomodate for miscalulation of frames
end

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



