import glob
import os

# # video gallery
# fnames = sorted(glob.glob('/Users/jingweim/Documents/VidPanos/vidpanos/static/images/real_results/*input.mp4'))
# for idx, in_fname in enumerate(fnames):
#     in_fname = in_fname.replace('/Users/jingweim/Documents/VidPanos/vidpanos', '.')
#     out_fname = in_fname.replace('input.mp4', 'ours_lumiere.mp4')
#     thumb_fname = in_fname.replace('input.mp4', 'thumb.jpg')
#     print(f'<div class="thumbnail active" data-video1="{in_fname}" data-video2="{out_fname}">')
#     print(f'    <img src="{thumb_fname}" alt="Video {idx+1}">')
#     print('</div>')

# results carousel
fnames = sorted(os.listdir('/Users/jingweim/Documents/VidPanos/vidpanos/static/images/flow_baselines'))
for idx, fname in enumerate(fnames):
    print(f'<div class="item item-{idx+1}" style="display: flex; flex-direction: column; align-items: center;">')
    print(f'    <video src="./static/images/flow_baselines/{fname}" autoplay controls muted loop playsinline></video>')
    print('</div>')
    
