import discord
from discord.ext import commands
import os, shutil
from google_images_download import google_images_download
from os import system
from discord.utils import get
import random
from google_images_download import google_images_download

#download issues
class image_cog(commands.Cog):
    def __init__(self, client):

        self.client = client
        self.download_folder = 'downloads'

        self.keywords = ["Spongebob","feet",]


        self.response = google_images_download.googleimagesdownload()
        self.arguments = {
            "keywords": self.keywords, 
            "limit": 5,
            "size":"medium",
            "no_directory": True
            }

        self.image_names = []
        #get the latest in the folder
        self.update_images()  


    @commands.command(name="get", help="Displays random image from the downloads")
    async def get(self, ctx):
        img = self.image_names[random.randint(0, len(self.image_names) - 1)]
        await ctx.send(file=discord.File(img))

    #Fix download func in case of spamming, try no_downloads
    def clear_folder(self):
        for filename in os.listdir(self.download_folder):
            file_path = os.path.join(self.download_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

    def update_images(self):
        self.image_names = []
        #store all the names to the files
        for filename in os.listdir(self.download_folder):
            self.image_names.append(os.path.join(self.download_folder, filename))

    @commands.command(name="search", help="searches for a message on google")
    async def search(self, ctx, *args):
        self.clear_folder()

        #fill the folder with new images
        self.arguments['keywords'] = " ".join(args)
        image = self.response.download(self.arguments)
        print(image)

        self.update_images()

        img = self.image_names[random.randint(0, len(self.image_names) - 1)]
        await ctx.send(file=discord.File(img))

def setup(client):
  client.add_cog(image_cog(client))