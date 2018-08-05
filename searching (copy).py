from os import path, walk
from fnmatch import fnmatch
from mutagen.easyid3 import EasyID3
import argparse

class MyLibrary():
	def InLocationAll(self,glob,directory):
		for (top, dirs, files) in walk(directory):
			for file in files:
	   			if fnmatch(file, glob):
					mp3FilePath = path.normpath(path.join(top,file))
					try:
		   				media = EasyID3(mp3FilePath)
		   				itm = media.items()
		   				data = { tagName:tagValue[0]   for tagName, tagValue in media.items()}
		   				title = "{title}"
		   				ftitle = title.format(**data)
		   				album = "{album}"
		   				falbum = album.format(**data)
		   				artist = "{artist}"
		   				fartist = artist.format(**data)
		   				
		   				print 'Found: \n'
		   				print("Title: "+ftitle+"\n")
		   				print("Artist: "+fartist+"\n")
		   				print("album: "+falbum+"\n")
		   				print('-----------------------------------------------------')
					except Exception as e:
		  				print("could not read: "+file+" "+str(e))

	def InLocationAlbum(self,glob,directory,albumm):
		for (top, dirs, files) in walk(directory):
			for file in files:
	   			if fnmatch(file, glob):
					mp3FilePath = path.normpath(path.join(top,file))
					try:
		   				media = EasyID3(mp3FilePath)
		   				itm = media.items()
		   				data = { tagName:tagValue[0]   for tagName, tagValue in media.items()}
		   				title = "{title}"
		   				ftitle = title.format(**data)
		   				album = "{album}"
		   				falbum = album.format(**data)
		   				artist = "{artist}"
		   				fartist = artist.format(**data)
		   				if falbum == albumm:
		   					print 'Found: \n'
		   					print("Title: "+ftitle+"\n")
		   					print("Artist: "+fartist+"\n")
		   					print("album: "+falbum+"\n")
		   					print('-----------------------------------------------------')
		   				else:
		   					print('no match found')
					except Exception as e:
		  				print("could not read: "+file+" "+str(e))


	def InLocationArtist(self,glob,directory,artistt):
		for (top, dirs, files) in walk(directory):
			for file in files:
	   			if fnmatch(file, glob):
					mp3FilePath = path.normpath(path.join(top,file))
					try:
		   				media = EasyID3(mp3FilePath)
		   				itm = media.items()
		   				data = { tagName:tagValue[0]   for tagName, tagValue in media.items()}
		   				title = "{title}"
		   				ftitle = title.format(**data)
		   				album = "{album}"
		   				falbum = album.format(**data)
		   				artist = "{artist}"
		   				fartist = artist.format(**data)
		   				if fartist == artistt:
		   					print 'Found: \n'
		   					print("Title: "+ftitle+"\n")
		   					print("Artist: "+fartist+"\n")
		   					print("album: "+falbum+"\n")
		   					print('-----------------------------------------------------')

		   				else:
		   					print('no match found')
					except Exception as e:
		  				#print("could not read: "+file+"\n")
		  				print("could not read: "+file+" "+str(e))


	def InLocation(self,glob,directory,artistt,albumm):
		for (top, dirs, files) in walk(directory):
			for file in files:
	   			if fnmatch(file, glob):
					mp3FilePath = path.normpath(path.join(top,file))
					try:
		   				media = EasyID3(mp3FilePath)
		   				itm = media.items()
		   				data = { tagName:tagValue[0]   for tagName, tagValue in media.items()}
		   				title = "{title}"
		   				ftitle = title.format(**data)
		   				album = "{album}"
		   				falbum = album.format(**data)
		   				artist = "{artist}"
		   				fartist = artist.format(**data)
		   				if fartist == artistt and falbum == albumm:
		   					print 'Found: \n'
		   					print("Title: "+ftitle+"\n")
		   					print("Artist: "+fartist+"\n")
		   					print("album: "+falbum+"\n")
		   					print('-----------------------------------------------------')

		   				else:
		   					print('no match found')
					except Exception as e:
		  				print("could not read: "+file+" "+str(e))





if __name__ == "__main__":
	lib = MyLibrary()
	parser = argparse.ArgumentParser()
	parser.add_argument('--loc',help='Location of the audio files')
	parser.add_argument('--artist',help='Displays music matching the artist')
	parser.add_argument('--album',help='Displays music matching the album')
	args = parser.parse_args()
	if args.artist and args.album:
		if args.loc:
			lib.InLocation("*.mp3",args.loc,args.artist,args.album)
		else:
			print('--loc : for location is mandatory argument')
	if args.artist:
		if args.loc:
			lib.InLocationArtist("*.mp3",args.loc,args.artist)
		else:
			print('--loc : for location is mandatory argument')
	if args.album:
		if args.loc:
			lib.InLocationAlbum("*.mp3",args.loc,args.album)
		else:
			print('--loc : for location is mandatory argument')
		
	if not args.album and not args.artist:
		if args.loc:
			lib.InLocationAll("*.mp3",args.loc)
		else:
			print('--loc: for location is mandatory argument')
	