import constval
from aioffmpeg.h264video import H264Video
from aioffmpeg.cmd_opts import H264EncoderArgs, FfmpegCmdModel

import pytest
import os
import random


@pytest.mark.asyncio
async def test_scale_video_qsv_aio():
    """
    测试视频缩放
    :return:
    """
    print('')
    h264_obj = H264Video(constval.VIDEO, constval.OUTPUT_DIR, aio=True)
    print('current work dir', os.path.abspath(os.getcwd()))
    home_dir = os.path.abspath(os.getenv('HOME'))
    scaled_obj, stderr = await h264_obj.cmd_do_aio(f'{home_dir:}', 'mp4', FfmpegCmdModel.scale_video_qsv,
                                                   target_height=random.randint(300, 1000),
                                                   target_videobitrate=random.randint(100, 400))
    assert scaled_obj is not None and stderr == ''
    print('H264Video object info:', scaled_obj)
    print(f'out put video width:{scaled_obj.video_width:d},video height:{scaled_obj.video_height:d},'
          f'video bit rate:{scaled_obj.video_bitrate:d}')


def test_scale_video_qsv():
    """
    测试视频缩放
    :return:
    """
    print('')
    h264_obj = H264Video(constval.VIDEO, constval.OUTPUT_DIR, aio=False)
    assert not hasattr(h264_obj, 'cmd_do_aio')
    print('current work dir', os.path.abspath(os.getcwd()))
    home_dir = os.path.abspath(os.getenv('HOME'))
    scaled_obj, stderr = h264_obj.cmd_do(f'{home_dir:s}', 'mp4', FfmpegCmdModel.scale_video_qsv,
                                         target_width=random.randint(700, 1000),
                                         target_height=random.randint(300, 1000),
                                         target_videobitrate=random.randint(100, 400))
    assert scaled_obj is not None and stderr == ''
    print('H264Video object info:', scaled_obj)
    print(f'out put video width:{scaled_obj.video_width:d},video height:{scaled_obj.video_height:d},'
          f'video bit rate:{scaled_obj.video_bitrate:d}')
