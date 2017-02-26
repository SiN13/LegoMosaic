import os

import PIL.Image as Image

import LegoMosaic.const


color_palette = [ #LegoMosaic.const.COLOR_YELLOW,
                  LegoMosaic.const.COLOR_WHITE,
                  LegoMosaic.const.COLOR_GREY_LIGHT,
                  LegoMosaic.const.COLOR_GREY_DARK,
                  LegoMosaic.const.COLOR_BLACK ]


def process_image( image_path ):
	source_image = Image.open( image_path )
	source_size = source_image.size
	source_image = source_image.resize( ( 48, 48 ) )

	output_image = source_image.convert( 'RGB' ).convert( 'P', palette = Image.ADAPTIVE, colors = len( color_palette ) )
	#output_image.putpalette( [ i for color in color_palette for i in color ] )

	output_image = output_image.resize( source_size )

	output_image.save( image_path + '.output.gif' )


def run( ):
	for image_path in LegoMosaic.const.TEST_FACES:
		process_image( image_path )
