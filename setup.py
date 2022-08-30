from distutils.core import setup

with open("README.rst", "r") as fh:
	long_description = fh.read()

setup(
	name = 'fake-blender-api-2.79',
	version = '0.4.0',

	packages = [
		"aud",

		"bge",
		"bge/app",
		"bge/constraints",
		"bge/events",
		"bge/logic",
		"bge/render",
		"bge/texture",
		"bge/types",

		"bgl",
		"blf",
		"bmesh",

		"bpy",
		"bpy/app",
		"bpy/ops",
		"bpy/utils",

		"bpy_extras",

		"freestyle",
		"freestyle/utils",

		"gpu",
		"idprop",

		"mathutils",
		"mathutils/noise"
	],

	license='GPLv3',
	description = "Fake Blender 2.79 Python API for code completion, including BGE",
	long_description=long_description,
	long_description_content_type="text/x-rst",
	author = 'Joel Gomes da Silva',
	author_email = 'joelgomes1994@hotmail.com',
	url = 'https://github.com/bgempire/fake-blender-api-2.79',
	download_url = 'https://github.com/bgempire/fake-blender-api-2.79/archive/0.3.tar.gz',

	keywords = [
		'blender',
		'bge',
		'upbge',
		'api',
		'3d',
		'bpy',
		'mathutils',
		'code',
		'completion',
		'autocomplete'
	],

	install_requires = [
		'typing'
	],

	classifiers=[
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Multimedia :: Graphics :: 3D Modeling',
		'Topic :: Multimedia :: Graphics :: 3D Rendering',
		'Topic :: Text Editors :: Integrated Development Environments (IDE)',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
		'Programming Language :: Python :: 3'
	]
)