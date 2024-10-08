from api.projects.athlete_progan.model import Generator, Critic
import torch
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt
import random
import os
from scipy.stats import truncnorm
# ADARSH HACK from upscale import upscale_image
#from basicsr.archs.rrdbnet_arch import RRDBNet
#from realesrgan import RealESRGANer
#from gfpgan import GFPGANer

def gen_images(team, skin_tone, build):
    num_images = 9
    bg_tile = 20
    upscale_factor = 2

    # critic_path = 'critic.pth'
    image_size = 128

    teams = ['ARI', 'ARI-2', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE', 'DAL', 'DEN',
             'DET', 'GB', 'HOU', 'IND', 'JAX', 'JAX-2', 'KC', 'MIA', 'MIN', 'NE', 'NE-2',
             'NO', 'NYG', 'NYJ', 'OAK', 'PHI', 'PIT', 'SD', 'SD-2', 'SEA', 'SF', 'STL',
             'STL-2', 'STL-3', 'TB', 'TB-2', 'TEN', 'TEN-2', 'WAS']
    if team != 'any':
        team_idx = teams.index(team)
        team_tensor = torch.tensor([team_idx] * num_images)
    else:
        team_tensor = torch.tensor([random.randint(0, len(teams) - 1) for i in range(num_images)])

    builds = ['light', 'medium', 'heavy']
    if build != 'any':
        build_idx = builds.index(build)
        build_tensor = torch.tensor([build_idx] * num_images)
    else:
        build_tensor = torch.tensor([random.randint(0, len(builds) - 1) for i in range(num_images)])

    skin_tones = ['very-dark', 'dark', 'neutral', 'fair', 'very-fair']
    if skin_tone != 'any':
        skin_tone_idx = skin_tones.index(skin_tone)
        skin_tone_tensor = torch.tensor([skin_tone_idx] * num_images)
    else:
        skin_tone_tensor = torch.tensor([random.randint(0, len(skin_tones) - 1) for i in range(num_images)])

    flattened_noise = truncnorm.rvs(-1, 1, size=num_images * 32)
    noise = torch.tensor(flattened_noise, dtype=torch.float).view((num_images, 32, 1, 1))

    generator_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'generator.pth')
    netG = Generator(32, 256, 16)
    netG.load_state_dict(torch.load(generator_path))

    fake = netG(noise, team_tensor, build_tensor, skin_tone_tensor, alpha=1, image_size=image_size)
    return fake
