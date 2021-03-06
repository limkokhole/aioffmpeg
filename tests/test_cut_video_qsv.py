import constval
from aioffmpeg.h264video import H264Video
from aioffmpeg.cmd_opts import H264EncoderArgs, FfmpegCmdModel

import pytest
import os
import random

@pytest.mark.asyncio
async def test_cut_video_qsv_aio():
    """
    测试视频缩放
    :return:
    """
    print('')
    h264_obj = H264Video(constval.VIDEO, constval.OUTPUT_DIR, aio=True)
    start_time = random.random() * 100
    last_time = random.randint(int(start_time)+1, 1000)
    print('current work dir', os.path.abspath(os.getcwd()))
    print(f'start_time: {start_time:f}, last_time: {last_time:d}')
    print(start_time, last_time)
    home_dir = os.path.abspath(os.getenv('HOME'))
    cuted_video, stderr = await h264_obj.cmd_do_aio(f'{home_dir:s}', 'mp4', FfmpegCmdModel.cut_video_qsv,
                                                    start_time=start_time,
                                                    last_time=last_time,
                                                    target_height=random.randint(100,300),
                                                    target_videobitrate=500)

    assert cuted_video is not None and stderr == ''
    print('H264Video object info:', cuted_video)
    print(f'out put video width:{cuted_video.video_width:d},video height:{cuted_video.video_height:d},'
          f'video bit rate:{cuted_video.video_bitrate:d}')

def test_cut_video():
    """
    测试视频缩放
    :return:
    """
    print('')
    h264_obj = H264Video(constval.VIDEO, constval.OUTPUT_DIR, aio=False)
    start_time = random.random() * 100
    last_time = random.randint(int(start_time)+1, 1000)
    assert not hasattr(h264_obj, 'cmd_do_aio')
    print('current work dir', os.path.abspath(os.getcwd()))
    print(f'start_time: {start_time:f}, last_time: {last_time:d}')
    home_dir = os.path.abspath(os.getenv('HOME'))
    cuted_video, stderr = h264_obj.cmd_do(f'{home_dir:s}', 'mp4', FfmpegCmdModel.cut_video_qsv,
                                          start_time=start_time,
                                          last_time=last_time,
                                          target_height=random.randint(100,300),
                                          target_videobitrate=500)

    assert cuted_video is not None and stderr == ''
    print('H264Video object info:', cuted_video)
    print(f'out put video width:{cuted_video.video_width:d},video height:{cuted_video.video_height:d},'
          f'video bit rate:{cuted_video.video_bitrate:d}')
