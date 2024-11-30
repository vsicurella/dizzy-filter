#!/bin/python3

from PIL import Image
import sys
import os

def getArgs(args):
    num = len(args)

    for i in range(num):
        print('{}: {}'.format(i, args[i]))

    img_path=os.path.join(args[1])
    (img_dir, img_file)=img_path.split()

    (img_name, img_type)=str(img_file).split('.')
    img_type='png'

    if not os.path.exists(img_path):
        raise Exception('Invalid input file')

    space = args[2] if args[2] else "RGB"

    return {
        "path": img_path,
        "dir": img_dir,
        "file": img_file,
        "name": img_name,
        "type": img_type,
        "space": space
    }  

def getProperties(options):
    print("getProperties")
    image=Image.open(options['path'])
    # img_size=`identify -ping -format '%w %h' $img_path`
    # width=$((${img_size#*\ }))
    # height=$((${img_size%\ *}))
    # echo width $width
    # echo height $height

    # face_result=`face_detection $img_path`
    # face_coords=("${(@s:,:)face_result}")
    # echo face_result $face_result
    # echo face_coords $face_coords

    # top_y=$((${face_coords[2]}))
    # top_x=$((${face_coords[3]}))
    # bot_y=$((${face_coords[4]}))
    # bot_x=$((${face_coords[5]}))

    # center_x=$((($top_x + $bot_x) * 0.5))
    # center_y=$((($top_y + $bot_y) * 0.5))

    # # dx=$(($top_x-$bot_x))
    # # dy=$(($top_y-$bot_y))
    # dx=$(($top_x-$center_x))
    # dy=$(($top_y-$center_y))
    # dd=$((($dx*$dx+$dy*$dy)))
    # radius=`awk "BEGIN {printf \"%.2f\n\", sqrt($dd)}"`
    # # radius=$(($radius_t*0.5))

    # rr=$(($radius*0.8))

    # # echo top_y $top_y
    # # echo top_x $top_x
    # # echo bot_y $bot_y
    # # echo bot_x $bot_x

    # # echo center $center_x $center_y
    # # echo dd $dd
    # # echo radius $radius

def createMasks(options, properties):
    print("createMasks")
    # face_mask_path=${img_dir}/face_mask.${img_type}
    # face_mask_blur=${img_dir}/face_mask_blur.${img_type}

    # blur_radius=$(($rr*0.5))

    # # magick -size ${height}x${width} xc:black -fill white -draw "ellipse ${center_x},${center_y} ${rr},${rr} 0,360" ${face_mask_path}
    # # magick ${face_mask_path} -blur 0x${blur_radius} ${face_mask_blur}

    # bg_mask_path=${img_dir}/bg_mask.${img_type}
    # bg_mask_blur=${img_dir}/bg_mask_blur.${img_type}

    # # magick -size ${height}x${width} xc:white -fill black -draw "ellipse ${center_x},${center_y} ${rr},${rr} 0,360" ${bg_mask_path}
    # # magick ${bg_mask_path} -blur 0x${blur_radius} ${bg_mask_blur}

def doDistorts(options, properties, masks):
    print("doDistorts")
    # face centered
    # centerp_x=$(($width-$center_x))
    # centerp_y=$(($height-$center_y))

    # echo centerp_x $centerp_x
    # echo centerp_y $centerp_y

    # dt_x=$((0))
    # dt_y=$((0))

    # if [[ $center_x -lt $centerp_x ]]; then
    #     dt_w=$(($centerp_x-$center_x))
    #     dt_x=$dt_w
    # else
    #     dt_w=$(($center_x-$centerp_x))
    # fi

    # if [[ $center_y -lt $centerp_y ]]; then
    #     dt_h=$(($centerp_y-$center_y))
    #     dt_y=$dt_h
    # else
    #     dt_h=$(($center_y-$centerp_y))
    # fi

    # width_rs=$(($width+$dt_w))
    # height_rs=$(($height+$dt_h))

    # # echo dt_x $dt_x
    # # echo dt_y $dt_y
    # # echo dt_w $dt_w
    # # echo dt_h $dt_h

    # # echo width_rs $width_rs
    # # echo height_rs $height_rs

    # img_centered=${img_dir}/img_centered.${img_type}
    # # magick -size ${height_rs}x${width_rs} xc:black \
    # #        -draw "image over ${dt_x},${dt_y} 0,0 '${img_path}'" \
    # #         ${img_centered}

    # # img_imploded=$img_dir/img_imploded.${img_type}
    # # magick  $img_centered \
    # #         -implode -0.125 \
    # #         $img_imploded

    # implode_scale=$((3.0/4))
    # implode_1=$((1.0/24*$implode_scale))
    # implode_2=$((1.0/20*$implode_scale))
    # implode_3=$((1.0/16*$implode_scale))
    # implode_4=$((1.0/12*$implode_scale))

    # # echo implode_1 $implode_1
    # # echo implode_2 $implode_2
    # # echo implode_3 $implode_3
    # # echo implode_4 $implode_4

    # implode_blur_radius_1=$(($radius*$implode_1))
    # implode_blur_radius_2=$(($radius*$implode_2))
    # implode_blur_radius_3=$(($radius*$implode_3))
    # implode_blur_radius_4=$(($radius*$implode_4))

    # # echo implode_blur_radius_1 $implode_blur_radius_1
    # # echo implode_blur_radius_2 $implode_blur_radius_2
    # # echo implode_blur_radius_3 $implode_blur_radius_3
    # # echo implode_blur_radius_4 $implode_blur_radius_4

    # img_imploded_blur_1=$img_dir/img_imploded_blur_1.${img_type}
    # magick  $img_centered \
    #         -implode "-${implode_1}" \
    #         -crop ${height}x${width}+${dt_x}+${dt_y}+\! \
    #         -blur 0x${implode_blur_radius_1} \
    #         $img_imploded_blur_1

    # img_imploded_blur_2=$img_dir/img_imploded_blur_2.${img_type}
    # magick  $img_centered \
    #         -implode "-${implode_2}" \
    #         -crop ${height}x${width}+${dt_x}+${dt_y}+\! \
    #         -blur 0x${implode_blur_radius_2} \
    #         $img_imploded_blur_2

    # img_imploded_blur_3=$img_dir/img_imploded_blur_3.${img_type}
    # magick  $img_centered \
    #         -implode "-${implode_3}" \
    #         -crop ${height}x${width}+${dt_x}+${dt_y}+\! \
    #         -blur 0x${implode_blur_radius_3} \
    #         $img_imploded_blur_3

    # img_imploded_blur_4=$img_dir/img_imploded_blur_4.${img_type}
    # magick  $img_centered \
    #         -implode "-${implode_4}" \
    #         -crop ${height}x${width}+${dt_x}+${dt_y}+\! \
    #         -blur 0x${implode_blur_radius_4} \
    #         $img_imploded_blur_4


    # magick  $img_path \
    #         -crop ${height}x${width}+0+0\! \
    #         -colorspace $space \
    #         -separate $img_dir/${img_name}_${space}_%d.${img_type}

    # img_imploded_blur1_RGB=$img_dir/img_imploded_blur1_RGB
    # img_imploded_blur2_RGB=$img_dir/img_imploded_blur2_RGB
    # img_imploded_blur3_RGB=$img_dir/img_imploded_blur3_RGB
    # img_imploded_blur4_RGB=$img_dir/img_imploded_blur4_RGB

    # magick $img_imploded_blur_1 -colorspace $space -separate $img_imploded_blur1_RGB%d.${img_type}
    # magick $img_imploded_blur_2 -colorspace $space -separate $img_imploded_blur2_RGB%d.${img_type}
    # magick $img_imploded_blur_3 -colorspace $space -separate $img_imploded_blur3_RGB%d.${img_type}
    # magick $img_imploded_blur_4 -colorspace $space -separate $img_imploded_blur4_RGB%d.${img_type}

    # dist_scale=$((1))
    # rotate_max=$((7*$dist_scale))
    # tx_max=$((4*$dist_scale))
    # ty_max=$((4*$dist_scale))

    # rotate_off=$(($rotate_max*0.5))
    # tx_off=$(($tx_max*0.5))
    # ty_off=$(($ty_max*0.5))

    # for blur in 1 2 3 4; do
    #     for c in 0 1 2; do
    #         layer_name=img_imploded_blur${blur}_RGB${c}
    #         layer=$img_dir/$layer_name.${img_type}
    #         echo layer $layer
    #         rand=$(($RANDOM))
    #         rotate=$(($rand / 32767.0 * $rotate_max - $rotate_off))
    #         echo rotate $rotate
    #         rand=$(($RANDOM))
    #         t_x=$(($rand / 32767.0 * $tx_max - $tx_off))
    #         echo t_x $t_x
    #         rand=$(($RANDOM))
    #         t_y=$(($rand / 32767.0 * $ty_max - $ty_off))
    #         echo t_y $t_y
    #         magick $layer -rotate $rotate \
    #                 -crop ${height}x${width}+$t_x+$t_y\! \
    #                 $img_dir/${layer_name}_dist.${img_type}
    #     done

    #     imgR=$img_dir/img_imploded_blur${blur}_RGB0_dist.${img_type}
    #     imgG=$img_dir/img_imploded_blur${blur}_RGB1_dist.${img_type}
    #     imgB=$img_dir/img_imploded_blur${blur}_RGB2_dist.${img_type}
    #     imgRGBdist=$img_dir/img_RGBdist${blur}.${img_type}

    #     # echo imgR $imgR
    #     # echo imgG $imgG
    #     # echo imgB $imgB

    #     magick $imgR $imgG $imgB -set colorspace RGB -combine $imgRGBdist

    #     # echo imgRGBdist $imgRGBdist
    #     # echo
    # done

    # imgRGBdist1=$img_dir/img_RGBdist1.${img_type}
    # imgRGBdist2=$img_dir/img_RGBdist2.${img_type}
    # imgRGBdist3=$img_dir/img_RGBdist3.${img_type}
    # imgRGBdist4=$img_dir/img_RGBdist4.${img_type}

def combineDistorts(options, properties, masks, distorts):
    # magick -background none \
    #         \( $imgRGBdist1 -alpha on -channel a -evaluate multiply 0.5 +channel \) \
    #         \( $imgRGBdist2 -alpha on -channel a -evaluate multiply 0.25 +channel \) \
    #         \( $imgRGBdist3 -alpha on -channel a -evaluate multiply 0.15 +channel \) \
    #         \( $imgRGBdist4 -alpha on -channel a -evaluate multiply 0.10 +channel \) \
    #         -flatten PNG32:${img_dir}/img_dist.${img_type}
    print('combineDistorts')


def main(args):
    options = getArgs(args)
    properties = getProperties(options)
    masks = createMasks(options, properties)
    distorts = doDistorts(options, properties, masks)
    combineDistorts(options, properties, masks, distorts)


if __name__ == '__main__':
    main(sys.argv)
