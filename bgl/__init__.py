import sys
import typing
import bpy


class Buffer:
    '''The Buffer object is simply a block of memory that is delineated and initialized by the user. Many OpenGL functions return data to a C-style pointer, however, because this is not possible in python the Buffer object can be used to this end. Wherever pointer notation is used in the OpenGL functions the Buffer object can be used in it's bgl wrapper. In some instances the Buffer object will need to be initialized with the template parameter, while in other instances the user will want to create just a blank buffer which will be zeroed by default. '''

    dimensions = None
    '''The number of dimensions of the Buffer. '''

    def to_list(self, ):
        '''The contents of the Buffer as a python list. 

        '''
        pass

    def __init__(self,
                 type: int,
                 dimensions: typing.List[int],
                 template: typing.List['bpy.context.object'] = None
                 ) -> 'bpy.context.object':
        '''This will create a new Buffer object for use with other bgl OpenGL commands. Only the type of argument to store in the buffer and the dimensions of the buffer are necessary. Buffers are zeroed by default unless a template is supplied, in which case the buffer is initialized to the template. 

        :param type: The format to store data in. The type should be one of GL_BYTE, GL_SHORT, GL_INT, or GL_FLOAT. 
        :type type: int
        :param dimensions: If the dimensions are specified as an int a linear array will be created for the buffer. If a sequence is passed for the dimensions, the buffer becomes n-Dimensional, where n is equal to the number of parameters passed in the sequence. Example: [256,2] is a two- dimensional buffer while [256,256,4] creates a three- dimensional buffer. You can think of each additional dimension as a sub-item of the dimension to the left. i.e. [10,2] is a 10 element array each with 2 sub-items. [(0,0), (0,1), (1,0), (1,1), (2,0), …] etc. 
        :type dimensions: typing.List[int]
        :param template: A sequence of matching dimensions which will be used to initialize the Buffer. If a template is not passed in all fields will be initialized to 0. 
        :type template: typing.List['bpy.context.object']
        :rtype: 'bpy.context.object'
        :return:  The newly created buffer as a PyObject. 
        '''
        pass


GL_ACTIVE_ATTRIBUTES: float = None

GL_ACTIVE_ATTRIBUTE_MAX_LENGTH: float = None

GL_ACTIVE_TEXTURE: float = None

GL_ACTIVE_UNIFORMS: float = None

GL_ACTIVE_UNIFORM_BLOCKS: float = None

GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH: float = None

GL_ACTIVE_UNIFORM_MAX_LENGTH: float = None

GL_ALIASED_LINE_WIDTH_RANGE: float = None

GL_ALPHA: float = None

GL_ALREADY_SIGNALED: float = None

GL_ALWAYS: float = None

GL_AND: float = None

GL_AND_INVERTED: float = None

GL_AND_REVERSE: float = None

GL_ANY_SAMPLES_PASSED: float = None

GL_ARRAY_BUFFER: float = None

GL_ARRAY_BUFFER_BINDING: float = None

GL_ATTACHED_SHADERS: float = None

GL_BACK: float = None

GL_BACK_LEFT: float = None

GL_BACK_RIGHT: float = None

GL_BGR: float = None

GL_BGRA: float = None

GL_BGRA_INTEGER: float = None

GL_BGR_INTEGER: float = None

GL_BLEND: float = None

GL_BLEND_DST: float = None

GL_BLEND_DST_ALPHA: float = None

GL_BLEND_DST_RGB: float = None

GL_BLEND_EQUATION_ALPHA: float = None

GL_BLEND_EQUATION_RGB: float = None

GL_BLEND_SRC: float = None

GL_BLEND_SRC_ALPHA: float = None

GL_BLEND_SRC_RGB: float = None

GL_BLUE: float = None

GL_BLUE_INTEGER: float = None

GL_BOOL: float = None

GL_BOOL_VEC2: float = None

GL_BOOL_VEC3: float = None

GL_BOOL_VEC4: float = None

GL_BUFFER_ACCESS: float = None

GL_BUFFER_ACCESS_FLAGS: float = None

GL_BUFFER_MAPPED: float = None

GL_BUFFER_MAP_LENGTH: float = None

GL_BUFFER_MAP_OFFSET: float = None

GL_BUFFER_MAP_POINTER: float = None

GL_BUFFER_SIZE: float = None

GL_BUFFER_USAGE: float = None

GL_BYTE: float = None

GL_CCW: float = None

GL_CLAMP_READ_COLOR: float = None

GL_CLAMP_TO_BORDER: float = None

GL_CLAMP_TO_EDGE: float = None

GL_CLEAR: float = None

GL_CLIP_DISTANCE0: float = None

GL_CLIP_DISTANCE1: float = None

GL_CLIP_DISTANCE2: float = None

GL_CLIP_DISTANCE3: float = None

GL_CLIP_DISTANCE4: float = None

GL_CLIP_DISTANCE5: float = None

GL_CLIP_DISTANCE6: float = None

GL_CLIP_DISTANCE7: float = None

GL_COLOR: float = None

GL_COLOR_ATTACHMENT0: float = None

GL_COLOR_ATTACHMENT1: float = None

GL_COLOR_ATTACHMENT10: float = None

GL_COLOR_ATTACHMENT11: float = None

GL_COLOR_ATTACHMENT12: float = None

GL_COLOR_ATTACHMENT13: float = None

GL_COLOR_ATTACHMENT14: float = None

GL_COLOR_ATTACHMENT15: float = None

GL_COLOR_ATTACHMENT16: float = None

GL_COLOR_ATTACHMENT17: float = None

GL_COLOR_ATTACHMENT18: float = None

GL_COLOR_ATTACHMENT19: float = None

GL_COLOR_ATTACHMENT2: float = None

GL_COLOR_ATTACHMENT20: float = None

GL_COLOR_ATTACHMENT21: float = None

GL_COLOR_ATTACHMENT22: float = None

GL_COLOR_ATTACHMENT23: float = None

GL_COLOR_ATTACHMENT24: float = None

GL_COLOR_ATTACHMENT25: float = None

GL_COLOR_ATTACHMENT26: float = None

GL_COLOR_ATTACHMENT27: float = None

GL_COLOR_ATTACHMENT28: float = None

GL_COLOR_ATTACHMENT29: float = None

GL_COLOR_ATTACHMENT3: float = None

GL_COLOR_ATTACHMENT30: float = None

GL_COLOR_ATTACHMENT31: float = None

GL_COLOR_ATTACHMENT4: float = None

GL_COLOR_ATTACHMENT5: float = None

GL_COLOR_ATTACHMENT6: float = None

GL_COLOR_ATTACHMENT7: float = None

GL_COLOR_ATTACHMENT8: float = None

GL_COLOR_ATTACHMENT9: float = None

GL_COLOR_BUFFER_BIT: float = None

GL_COLOR_CLEAR_VALUE: float = None

GL_COLOR_LOGIC_OP: float = None

GL_COLOR_WRITEMASK: float = None

GL_COMPARE_REF_TO_TEXTURE: float = None

GL_COMPILE_STATUS: float = None

GL_COMPRESSED_RED: float = None

GL_COMPRESSED_RED_RGTC1: float = None

GL_COMPRESSED_RG: float = None

GL_COMPRESSED_RGB: float = None

GL_COMPRESSED_RGBA: float = None

GL_COMPRESSED_RG_RGTC2: float = None

GL_COMPRESSED_SIGNED_RED_RGTC1: float = None

GL_COMPRESSED_SIGNED_RG_RGTC2: float = None

GL_COMPRESSED_SRGB: float = None

GL_COMPRESSED_SRGB_ALPHA: float = None

GL_COMPRESSED_TEXTURE_FORMATS: float = None

GL_CONDITION_SATISFIED: float = None

GL_CONSTANT_ALPHA: float = None

GL_CONSTANT_COLOR: float = None

GL_CONTEXT_COMPATIBILITY_PROFILE_BIT: float = None

GL_CONTEXT_CORE_PROFILE_BIT: float = None

GL_CONTEXT_FLAGS: float = None

GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT: float = None

GL_CONTEXT_PROFILE_MASK: float = None

GL_COPY: float = None

GL_COPY_INVERTED: float = None

GL_COPY_READ_BUFFER: float = None

GL_COPY_WRITE_BUFFER: float = None

GL_CULL_FACE: float = None

GL_CULL_FACE_MODE: float = None

GL_CURRENT_PROGRAM: float = None

GL_CURRENT_QUERY: float = None

GL_CURRENT_VERTEX_ATTRIB: float = None

GL_CW: float = None

GL_DECR: float = None

GL_DECR_WRAP: float = None

GL_DELETE_STATUS: float = None

GL_DEPTH: float = None

GL_DEPTH24_STENCIL8: float = None

GL_DEPTH32F_STENCIL8: float = None

GL_DEPTH_ATTACHMENT: float = None

GL_DEPTH_BUFFER_BIT: float = None

GL_DEPTH_CLAMP: float = None

GL_DEPTH_CLEAR_VALUE: float = None

GL_DEPTH_COMPONENT: float = None

GL_DEPTH_COMPONENT16: float = None

GL_DEPTH_COMPONENT24: float = None

GL_DEPTH_COMPONENT32: float = None

GL_DEPTH_COMPONENT32F: float = None

GL_DEPTH_FUNC: float = None

GL_DEPTH_RANGE: float = None

GL_DEPTH_STENCIL: float = None

GL_DEPTH_STENCIL_ATTACHMENT: float = None

GL_DEPTH_TEST: float = None

GL_DEPTH_WRITEMASK: float = None

GL_DITHER: float = None

GL_DONT_CARE: float = None

GL_DOUBLE: float = None

GL_DOUBLEBUFFER: float = None

GL_DRAW_BUFFER: float = None

GL_DRAW_BUFFER0: float = None

GL_DRAW_BUFFER1: float = None

GL_DRAW_BUFFER10: float = None

GL_DRAW_BUFFER11: float = None

GL_DRAW_BUFFER12: float = None

GL_DRAW_BUFFER13: float = None

GL_DRAW_BUFFER14: float = None

GL_DRAW_BUFFER15: float = None

GL_DRAW_BUFFER2: float = None

GL_DRAW_BUFFER3: float = None

GL_DRAW_BUFFER4: float = None

GL_DRAW_BUFFER5: float = None

GL_DRAW_BUFFER6: float = None

GL_DRAW_BUFFER7: float = None

GL_DRAW_BUFFER8: float = None

GL_DRAW_BUFFER9: float = None

GL_DRAW_FRAMEBUFFER: float = None

GL_DRAW_FRAMEBUFFER_BINDING: float = None

GL_DST_ALPHA: float = None

GL_DST_COLOR: float = None

GL_DYNAMIC_COPY: float = None

GL_DYNAMIC_DRAW: float = None

GL_DYNAMIC_READ: float = None

GL_ELEMENT_ARRAY_BUFFER: float = None

GL_ELEMENT_ARRAY_BUFFER_BINDING: float = None

GL_EQUAL: float = None

GL_EQUIV: float = None

GL_EXTENSIONS: float = None

GL_FALSE: float = None

GL_FASTEST: float = None

GL_FILL: float = None

GL_FIRST_VERTEX_CONVENTION: float = None

GL_FIXED_ONLY: float = None

GL_FLOAT: float = None

GL_FLOAT_32_UNSIGNED_INT_24_8_REV: float = None

GL_FLOAT_MAT2: float = None

GL_FLOAT_MAT2x3: float = None

GL_FLOAT_MAT2x4: float = None

GL_FLOAT_MAT3: float = None

GL_FLOAT_MAT3x2: float = None

GL_FLOAT_MAT3x4: float = None

GL_FLOAT_MAT4: float = None

GL_FLOAT_MAT4x2: float = None

GL_FLOAT_MAT4x3: float = None

GL_FLOAT_VEC2: float = None

GL_FLOAT_VEC3: float = None

GL_FLOAT_VEC4: float = None

GL_FRAGMENT_SHADER: float = None

GL_FRAGMENT_SHADER_DERIVATIVE_HINT: float = None

GL_FRAMEBUFFER: float = None

GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE: float = None

GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE: float = None

GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING: float = None

GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE: float = None

GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE: float = None

GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE: float = None

GL_FRAMEBUFFER_ATTACHMENT_LAYERED: float = None

GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME: float = None

GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE: float = None

GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE: float = None

GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE: float = None

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE: float = None

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER: float = None

GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL: float = None

GL_FRAMEBUFFER_BINDING: float = None

GL_FRAMEBUFFER_COMPLETE: float = None

GL_FRAMEBUFFER_DEFAULT: float = None

GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT: float = None

GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER: float = None

GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS: float = None

GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT: float = None

GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE: float = None

GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER: float = None

GL_FRAMEBUFFER_SRGB: float = None

GL_FRAMEBUFFER_UNDEFINED: float = None

GL_FRAMEBUFFER_UNSUPPORTED: float = None

GL_FRONT: float = None

GL_FRONT_AND_BACK: float = None

GL_FRONT_FACE: float = None

GL_FRONT_LEFT: float = None

GL_FRONT_RIGHT: float = None

GL_FUNC_ADD: float = None

GL_FUNC_REVERSE_SUBTRACT: float = None

GL_FUNC_SUBTRACT: float = None

GL_GEOMETRY_INPUT_TYPE: float = None

GL_GEOMETRY_OUTPUT_TYPE: float = None

GL_GEOMETRY_SHADER: float = None

GL_GEOMETRY_VERTICES_OUT: float = None

GL_GEQUAL: float = None

GL_GREATER: float = None

GL_GREEN: float = None

GL_GREEN_INTEGER: float = None

GL_HALF_FLOAT: float = None

GL_INCR: float = None

GL_INCR_WRAP: float = None

GL_INDEX: float = None

GL_INFO_LOG_LENGTH: float = None

GL_INT: float = None

GL_INTERLEAVED_ATTRIBS: float = None

GL_INT_2_10_10_10_REV: float = None

GL_INT_SAMPLER_1D: float = None

GL_INT_SAMPLER_1D_ARRAY: float = None

GL_INT_SAMPLER_2D: float = None

GL_INT_SAMPLER_2D_ARRAY: float = None

GL_INT_SAMPLER_2D_MULTISAMPLE: float = None

GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: float = None

GL_INT_SAMPLER_2D_RECT: float = None

GL_INT_SAMPLER_3D: float = None

GL_INT_SAMPLER_BUFFER: float = None

GL_INT_SAMPLER_CUBE: float = None

GL_INT_VEC2: float = None

GL_INT_VEC3: float = None

GL_INT_VEC4: float = None

GL_INVALID_ENUM: float = None

GL_INVALID_FRAMEBUFFER_OPERATION: float = None

GL_INVALID_INDEX: float = None

GL_INVALID_OPERATION: float = None

GL_INVALID_VALUE: float = None

GL_INVERT: float = None

GL_KEEP: float = None

GL_LAST_VERTEX_CONVENTION: float = None

GL_LEFT: float = None

GL_LEQUAL: float = None

GL_LESS: float = None

GL_LINE: float = None

GL_LINEAR: float = None

GL_LINEAR_MIPMAP_LINEAR: float = None

GL_LINEAR_MIPMAP_NEAREST: float = None

GL_LINES: float = None

GL_LINES_ADJACENCY: float = None

GL_LINE_LOOP: float = None

GL_LINE_SMOOTH: float = None

GL_LINE_SMOOTH_HINT: float = None

GL_LINE_STRIP: float = None

GL_LINE_STRIP_ADJACENCY: float = None

GL_LINE_WIDTH: float = None

GL_LINE_WIDTH_GRANULARITY: float = None

GL_LINE_WIDTH_RANGE: float = None

GL_LINK_STATUS: float = None

GL_LOGIC_OP_MODE: float = None

GL_LOWER_LEFT: float = None

GL_MAJOR_VERSION: float = None

GL_MAP_FLUSH_EXPLICIT_BIT: float = None

GL_MAP_INVALIDATE_BUFFER_BIT: float = None

GL_MAP_INVALIDATE_RANGE_BIT: float = None

GL_MAP_READ_BIT: float = None

GL_MAP_UNSYNCHRONIZED_BIT: float = None

GL_MAP_WRITE_BIT: float = None

GL_MAX: float = None

GL_MAX_3D_TEXTURE_SIZE: float = None

GL_MAX_ARRAY_TEXTURE_LAYERS: float = None

GL_MAX_CLIP_DISTANCES: float = None

GL_MAX_COLOR_ATTACHMENTS: float = None

GL_MAX_COLOR_TEXTURE_SAMPLES: float = None

GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS: float = None

GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS: float = None

GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS: float = None

GL_MAX_COMBINED_UNIFORM_BLOCKS: float = None

GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS: float = None

GL_MAX_CUBE_MAP_TEXTURE_SIZE: float = None

GL_MAX_DEPTH_TEXTURE_SAMPLES: float = None

GL_MAX_DRAW_BUFFERS: float = None

GL_MAX_DUAL_SOURCE_DRAW_BUFFERS: float = None

GL_MAX_ELEMENTS_INDICES: float = None

GL_MAX_ELEMENTS_VERTICES: float = None

GL_MAX_FRAGMENT_INPUT_COMPONENTS: float = None

GL_MAX_FRAGMENT_UNIFORM_BLOCKS: float = None

GL_MAX_FRAGMENT_UNIFORM_COMPONENTS: float = None

GL_MAX_GEOMETRY_INPUT_COMPONENTS: float = None

GL_MAX_GEOMETRY_OUTPUT_COMPONENTS: float = None

GL_MAX_GEOMETRY_OUTPUT_VERTICES: float = None

GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS: float = None

GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS: float = None

GL_MAX_GEOMETRY_UNIFORM_BLOCKS: float = None

GL_MAX_GEOMETRY_UNIFORM_COMPONENTS: float = None

GL_MAX_INTEGER_SAMPLES: float = None

GL_MAX_PROGRAM_TEXEL_OFFSET: float = None

GL_MAX_RECTANGLE_TEXTURE_SIZE: float = None

GL_MAX_RENDERBUFFER_SIZE: float = None

GL_MAX_SAMPLES: float = None

GL_MAX_SAMPLE_MASK_WORDS: float = None

GL_MAX_SERVER_WAIT_TIMEOUT: float = None

GL_MAX_TEXTURE_BUFFER_SIZE: float = None

GL_MAX_TEXTURE_IMAGE_UNITS: float = None

GL_MAX_TEXTURE_LOD_BIAS: float = None

GL_MAX_TEXTURE_SIZE: float = None

GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS: float = None

GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS: float = None

GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS: float = None

GL_MAX_UNIFORM_BLOCK_SIZE: float = None

GL_MAX_UNIFORM_BUFFER_BINDINGS: float = None

GL_MAX_VARYING_COMPONENTS: float = None

GL_MAX_VARYING_FLOATS: float = None

GL_MAX_VERTEX_ATTRIBS: float = None

GL_MAX_VERTEX_OUTPUT_COMPONENTS: float = None

GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS: float = None

GL_MAX_VERTEX_UNIFORM_BLOCKS: float = None

GL_MAX_VERTEX_UNIFORM_COMPONENTS: float = None

GL_MAX_VIEWPORT_DIMS: float = None

GL_MIN: float = None

GL_MINOR_VERSION: float = None

GL_MIN_PROGRAM_TEXEL_OFFSET: float = None

GL_MIRRORED_REPEAT: float = None

GL_MULTISAMPLE: float = None

GL_NAND: float = None

GL_NEAREST: float = None

GL_NEAREST_MIPMAP_LINEAR: float = None

GL_NEAREST_MIPMAP_NEAREST: float = None

GL_NEVER: float = None

GL_NICEST: float = None

GL_NONE: float = None

GL_NOOP: float = None

GL_NOR: float = None

GL_NOTEQUAL: float = None

GL_NO_ERROR: float = None

GL_NUM_COMPRESSED_TEXTURE_FORMATS: float = None

GL_NUM_EXTENSIONS: float = None

GL_OBJECT_TYPE: float = None

GL_ONE: float = None

GL_ONE_MINUS_CONSTANT_ALPHA: float = None

GL_ONE_MINUS_CONSTANT_COLOR: float = None

GL_ONE_MINUS_DST_ALPHA: float = None

GL_ONE_MINUS_DST_COLOR: float = None

GL_ONE_MINUS_SRC1_ALPHA: float = None

GL_ONE_MINUS_SRC1_COLOR: float = None

GL_ONE_MINUS_SRC_ALPHA: float = None

GL_ONE_MINUS_SRC_COLOR: float = None

GL_OR: float = None

GL_OR_INVERTED: float = None

GL_OR_REVERSE: float = None

GL_OUT_OF_MEMORY: float = None

GL_PACK_ALIGNMENT: float = None

GL_PACK_IMAGE_HEIGHT: float = None

GL_PACK_LSB_FIRST: float = None

GL_PACK_ROW_LENGTH: float = None

GL_PACK_SKIP_IMAGES: float = None

GL_PACK_SKIP_PIXELS: float = None

GL_PACK_SKIP_ROWS: float = None

GL_PACK_SWAP_BYTES: float = None

GL_PIXEL_PACK_BUFFER: float = None

GL_PIXEL_PACK_BUFFER_BINDING: float = None

GL_PIXEL_UNPACK_BUFFER: float = None

GL_PIXEL_UNPACK_BUFFER_BINDING: float = None

GL_POINT: float = None

GL_POINTS: float = None

GL_POINT_FADE_THRESHOLD_SIZE: float = None

GL_POINT_SIZE: float = None

GL_POINT_SPRITE_COORD_ORIGIN: float = None

GL_POLYGON_MODE: float = None

GL_POLYGON_OFFSET_FACTOR: float = None

GL_POLYGON_OFFSET_FILL: float = None

GL_POLYGON_OFFSET_LINE: float = None

GL_POLYGON_OFFSET_POINT: float = None

GL_POLYGON_OFFSET_UNITS: float = None

GL_POLYGON_SMOOTH: float = None

GL_POLYGON_SMOOTH_HINT: float = None

GL_PRIMITIVES_GENERATED: float = None

GL_PRIMITIVE_RESTART: float = None

GL_PRIMITIVE_RESTART_INDEX: float = None

GL_PROGRAM_POINT_SIZE: float = None

GL_PROVOKING_VERTEX: float = None

GL_PROXY_TEXTURE_1D: float = None

GL_PROXY_TEXTURE_1D_ARRAY: float = None

GL_PROXY_TEXTURE_2D: float = None

GL_PROXY_TEXTURE_2D_ARRAY: float = None

GL_PROXY_TEXTURE_2D_MULTISAMPLE: float = None

GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY: float = None

GL_PROXY_TEXTURE_3D: float = None

GL_PROXY_TEXTURE_CUBE_MAP: float = None

GL_PROXY_TEXTURE_RECTANGLE: float = None

GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION: float = None

GL_QUERY_BY_REGION_NO_WAIT: float = None

GL_QUERY_BY_REGION_WAIT: float = None

GL_QUERY_COUNTER_BITS: float = None

GL_QUERY_NO_WAIT: float = None

GL_QUERY_RESULT: float = None

GL_QUERY_RESULT_AVAILABLE: float = None

GL_QUERY_WAIT: float = None

GL_R11F_G11F_B10F: float = None

GL_R16: float = None

GL_R16F: float = None

GL_R16I: float = None

GL_R16UI: float = None

GL_R16_SNORM: float = None

GL_R32F: float = None

GL_R32I: float = None

GL_R32UI: float = None

GL_R3_G3_B2: float = None

GL_R8: float = None

GL_R8I: float = None

GL_R8UI: float = None

GL_R8_SNORM: float = None

GL_RASTERIZER_DISCARD: float = None

GL_READ_BUFFER: float = None

GL_READ_FRAMEBUFFER: float = None

GL_READ_FRAMEBUFFER_BINDING: float = None

GL_READ_ONLY: float = None

GL_READ_WRITE: float = None

GL_RED: float = None

GL_RED_INTEGER: float = None

GL_RENDERBUFFER: float = None

GL_RENDERBUFFER_ALPHA_SIZE: float = None

GL_RENDERBUFFER_BINDING: float = None

GL_RENDERBUFFER_BLUE_SIZE: float = None

GL_RENDERBUFFER_DEPTH_SIZE: float = None

GL_RENDERBUFFER_GREEN_SIZE: float = None

GL_RENDERBUFFER_HEIGHT: float = None

GL_RENDERBUFFER_INTERNAL_FORMAT: float = None

GL_RENDERBUFFER_RED_SIZE: float = None

GL_RENDERBUFFER_SAMPLES: float = None

GL_RENDERBUFFER_STENCIL_SIZE: float = None

GL_RENDERBUFFER_WIDTH: float = None

GL_RENDERER: float = None

GL_REPEAT: float = None

GL_REPLACE: float = None

GL_RG: float = None

GL_RG16: float = None

GL_RG16F: float = None

GL_RG16I: float = None

GL_RG16UI: float = None

GL_RG16_SNORM: float = None

GL_RG32F: float = None

GL_RG32I: float = None

GL_RG32UI: float = None

GL_RG8: float = None

GL_RG8I: float = None

GL_RG8UI: float = None

GL_RG8_SNORM: float = None

GL_RGB: float = None

GL_RGB10: float = None

GL_RGB10_A2: float = None

GL_RGB10_A2UI: float = None

GL_RGB12: float = None

GL_RGB16: float = None

GL_RGB16F: float = None

GL_RGB16I: float = None

GL_RGB16UI: float = None

GL_RGB16_SNORM: float = None

GL_RGB32F: float = None

GL_RGB32I: float = None

GL_RGB32UI: float = None

GL_RGB4: float = None

GL_RGB5: float = None

GL_RGB5_A1: float = None

GL_RGB8: float = None

GL_RGB8I: float = None

GL_RGB8UI: float = None

GL_RGB8_SNORM: float = None

GL_RGB9_E5: float = None

GL_RGBA: float = None

GL_RGBA12: float = None

GL_RGBA16: float = None

GL_RGBA16F: float = None

GL_RGBA16I: float = None

GL_RGBA16UI: float = None

GL_RGBA16_SNORM: float = None

GL_RGBA2: float = None

GL_RGBA32F: float = None

GL_RGBA32I: float = None

GL_RGBA32UI: float = None

GL_RGBA4: float = None

GL_RGBA8: float = None

GL_RGBA8I: float = None

GL_RGBA8UI: float = None

GL_RGBA8_SNORM: float = None

GL_RGBA_INTEGER: float = None

GL_RGB_INTEGER: float = None

GL_RG_INTEGER: float = None

GL_RIGHT: float = None

GL_SAMPLER_1D: float = None

GL_SAMPLER_1D_ARRAY: float = None

GL_SAMPLER_1D_ARRAY_SHADOW: float = None

GL_SAMPLER_1D_SHADOW: float = None

GL_SAMPLER_2D: float = None

GL_SAMPLER_2D_ARRAY: float = None

GL_SAMPLER_2D_ARRAY_SHADOW: float = None

GL_SAMPLER_2D_MULTISAMPLE: float = None

GL_SAMPLER_2D_MULTISAMPLE_ARRAY: float = None

GL_SAMPLER_2D_RECT: float = None

GL_SAMPLER_2D_RECT_SHADOW: float = None

GL_SAMPLER_2D_SHADOW: float = None

GL_SAMPLER_3D: float = None

GL_SAMPLER_BINDING: float = None

GL_SAMPLER_BUFFER: float = None

GL_SAMPLER_CUBE: float = None

GL_SAMPLER_CUBE_SHADOW: float = None

GL_SAMPLES: float = None

GL_SAMPLES_PASSED: float = None

GL_SAMPLE_ALPHA_TO_COVERAGE: float = None

GL_SAMPLE_ALPHA_TO_ONE: float = None

GL_SAMPLE_BUFFERS: float = None

GL_SAMPLE_COVERAGE: float = None

GL_SAMPLE_COVERAGE_INVERT: float = None

GL_SAMPLE_COVERAGE_VALUE: float = None

GL_SAMPLE_MASK: float = None

GL_SAMPLE_MASK_VALUE: float = None

GL_SAMPLE_POSITION: float = None

GL_SCISSOR_BOX: float = None

GL_SCISSOR_TEST: float = None

GL_SEPARATE_ATTRIBS: float = None

GL_SET: float = None

GL_SHADER_SOURCE_LENGTH: float = None

GL_SHADER_TYPE: float = None

GL_SHADING_LANGUAGE_VERSION: float = None

GL_SHORT: float = None

GL_SIGNALED: float = None

GL_SIGNED_NORMALIZED: float = None

GL_SMOOTH_LINE_WIDTH_GRANULARITY: float = None

GL_SMOOTH_LINE_WIDTH_RANGE: float = None

GL_SMOOTH_POINT_SIZE_GRANULARITY: float = None

GL_SMOOTH_POINT_SIZE_RANGE: float = None

GL_SRC1_COLOR: float = None

GL_SRC_ALPHA: float = None

GL_SRC_ALPHA_SATURATE: float = None

GL_SRC_COLOR: float = None

GL_SRGB: float = None

GL_SRGB8: float = None

GL_SRGB8_ALPHA8: float = None

GL_SRGB_ALPHA: float = None

GL_STATIC_COPY: float = None

GL_STATIC_DRAW: float = None

GL_STATIC_READ: float = None

GL_STENCIL: float = None

GL_STENCIL_ATTACHMENT: float = None

GL_STENCIL_BACK_FAIL: float = None

GL_STENCIL_BACK_FUNC: float = None

GL_STENCIL_BACK_PASS_DEPTH_FAIL: float = None

GL_STENCIL_BACK_PASS_DEPTH_PASS: float = None

GL_STENCIL_BACK_REF: float = None

GL_STENCIL_BACK_VALUE_MASK: float = None

GL_STENCIL_BACK_WRITEMASK: float = None

GL_STENCIL_BUFFER_BIT: float = None

GL_STENCIL_CLEAR_VALUE: float = None

GL_STENCIL_FAIL: float = None

GL_STENCIL_FUNC: float = None

GL_STENCIL_INDEX: float = None

GL_STENCIL_INDEX1: float = None

GL_STENCIL_INDEX16: float = None

GL_STENCIL_INDEX4: float = None

GL_STENCIL_INDEX8: float = None

GL_STENCIL_PASS_DEPTH_FAIL: float = None

GL_STENCIL_PASS_DEPTH_PASS: float = None

GL_STENCIL_REF: float = None

GL_STENCIL_TEST: float = None

GL_STENCIL_VALUE_MASK: float = None

GL_STENCIL_WRITEMASK: float = None

GL_STEREO: float = None

GL_STREAM_COPY: float = None

GL_STREAM_DRAW: float = None

GL_STREAM_READ: float = None

GL_SUBPIXEL_BITS: float = None

GL_SYNC_CONDITION: float = None

GL_SYNC_FENCE: float = None

GL_SYNC_FLAGS: float = None

GL_SYNC_FLUSH_COMMANDS_BIT: float = None

GL_SYNC_GPU_COMMANDS_COMPLETE: float = None

GL_SYNC_STATUS: float = None

GL_TEXTURE: float = None

GL_TEXTURE0: float = None

GL_TEXTURE1: float = None

GL_TEXTURE10: float = None

GL_TEXTURE11: float = None

GL_TEXTURE12: float = None

GL_TEXTURE13: float = None

GL_TEXTURE14: float = None

GL_TEXTURE15: float = None

GL_TEXTURE16: float = None

GL_TEXTURE17: float = None

GL_TEXTURE18: float = None

GL_TEXTURE19: float = None

GL_TEXTURE2: float = None

GL_TEXTURE20: float = None

GL_TEXTURE21: float = None

GL_TEXTURE22: float = None

GL_TEXTURE23: float = None

GL_TEXTURE24: float = None

GL_TEXTURE25: float = None

GL_TEXTURE26: float = None

GL_TEXTURE27: float = None

GL_TEXTURE28: float = None

GL_TEXTURE29: float = None

GL_TEXTURE3: float = None

GL_TEXTURE30: float = None

GL_TEXTURE31: float = None

GL_TEXTURE4: float = None

GL_TEXTURE5: float = None

GL_TEXTURE6: float = None

GL_TEXTURE7: float = None

GL_TEXTURE8: float = None

GL_TEXTURE9: float = None

GL_TEXTURE_1D: float = None

GL_TEXTURE_1D_ARRAY: float = None

GL_TEXTURE_2D: float = None

GL_TEXTURE_2D_ARRAY: float = None

GL_TEXTURE_2D_MULTISAMPLE: float = None

GL_TEXTURE_2D_MULTISAMPLE_ARRAY: float = None

GL_TEXTURE_3D: float = None

GL_TEXTURE_ALPHA_SIZE: float = None

GL_TEXTURE_ALPHA_TYPE: float = None

GL_TEXTURE_BASE_LEVEL: float = None

GL_TEXTURE_BINDING_1D: float = None

GL_TEXTURE_BINDING_1D_ARRAY: float = None

GL_TEXTURE_BINDING_2D: float = None

GL_TEXTURE_BINDING_2D_ARRAY: float = None

GL_TEXTURE_BINDING_2D_MULTISAMPLE: float = None

GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY: float = None

GL_TEXTURE_BINDING_3D: float = None

GL_TEXTURE_BINDING_BUFFER: float = None

GL_TEXTURE_BINDING_CUBE_MAP: float = None

GL_TEXTURE_BINDING_RECTANGLE: float = None

GL_TEXTURE_BLUE_SIZE: float = None

GL_TEXTURE_BLUE_TYPE: float = None

GL_TEXTURE_BORDER_COLOR: float = None

GL_TEXTURE_BUFFER: float = None

GL_TEXTURE_BUFFER_DATA_STORE_BINDING: float = None

GL_TEXTURE_COMPARE_FUNC: float = None

GL_TEXTURE_COMPARE_MODE: float = None

GL_TEXTURE_COMPRESSED: float = None

GL_TEXTURE_COMPRESSED_IMAGE_SIZE: float = None

GL_TEXTURE_COMPRESSION_HINT: float = None

GL_TEXTURE_CUBE_MAP: float = None

GL_TEXTURE_CUBE_MAP_NEGATIVE_X: float = None

GL_TEXTURE_CUBE_MAP_NEGATIVE_Y: float = None

GL_TEXTURE_CUBE_MAP_NEGATIVE_Z: float = None

GL_TEXTURE_CUBE_MAP_POSITIVE_X: float = None

GL_TEXTURE_CUBE_MAP_POSITIVE_Y: float = None

GL_TEXTURE_CUBE_MAP_POSITIVE_Z: float = None

GL_TEXTURE_CUBE_MAP_SEAMLESS: float = None

GL_TEXTURE_DEPTH: float = None

GL_TEXTURE_DEPTH_SIZE: float = None

GL_TEXTURE_DEPTH_TYPE: float = None

GL_TEXTURE_FIXED_SAMPLE_LOCATIONS: float = None

GL_TEXTURE_GREEN_SIZE: float = None

GL_TEXTURE_GREEN_TYPE: float = None

GL_TEXTURE_HEIGHT: float = None

GL_TEXTURE_INTERNAL_FORMAT: float = None

GL_TEXTURE_LOD_BIAS: float = None

GL_TEXTURE_MAG_FILTER: float = None

GL_TEXTURE_MAX_LEVEL: float = None

GL_TEXTURE_MAX_LOD: float = None

GL_TEXTURE_MIN_FILTER: float = None

GL_TEXTURE_MIN_LOD: float = None

GL_TEXTURE_RECTANGLE: float = None

GL_TEXTURE_RED_SIZE: float = None

GL_TEXTURE_RED_TYPE: float = None

GL_TEXTURE_SAMPLES: float = None

GL_TEXTURE_SHARED_SIZE: float = None

GL_TEXTURE_STENCIL_SIZE: float = None

GL_TEXTURE_SWIZZLE_A: float = None

GL_TEXTURE_SWIZZLE_B: float = None

GL_TEXTURE_SWIZZLE_G: float = None

GL_TEXTURE_SWIZZLE_R: float = None

GL_TEXTURE_SWIZZLE_RGBA: float = None

GL_TEXTURE_WIDTH: float = None

GL_TEXTURE_WRAP_R: float = None

GL_TEXTURE_WRAP_S: float = None

GL_TEXTURE_WRAP_T: float = None

GL_TIMEOUT_EXPIRED: float = None

GL_TIMEOUT_IGNORED: float = None

GL_TIMESTAMP: float = None

GL_TIME_ELAPSED: float = None

GL_TRANSFORM_FEEDBACK_BUFFER: float = None

GL_TRANSFORM_FEEDBACK_BUFFER_BINDING: float = None

GL_TRANSFORM_FEEDBACK_BUFFER_MODE: float = None

GL_TRANSFORM_FEEDBACK_BUFFER_SIZE: float = None

GL_TRANSFORM_FEEDBACK_BUFFER_START: float = None

GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN: float = None

GL_TRANSFORM_FEEDBACK_VARYINGS: float = None

GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH: float = None

GL_TRIANGLES: float = None

GL_TRIANGLES_ADJACENCY: float = None

GL_TRIANGLE_FAN: float = None

GL_TRIANGLE_STRIP: float = None

GL_TRIANGLE_STRIP_ADJACENCY: float = None

GL_TRUE: float = None

GL_UNIFORM_ARRAY_STRIDE: float = None

GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS: float = None

GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES: float = None

GL_UNIFORM_BLOCK_BINDING: float = None

GL_UNIFORM_BLOCK_DATA_SIZE: float = None

GL_UNIFORM_BLOCK_INDEX: float = None

GL_UNIFORM_BLOCK_NAME_LENGTH: float = None

GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER: float = None

GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER: float = None

GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER: float = None

GL_UNIFORM_BUFFER: float = None

GL_UNIFORM_BUFFER_BINDING: float = None

GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT: float = None

GL_UNIFORM_BUFFER_SIZE: float = None

GL_UNIFORM_BUFFER_START: float = None

GL_UNIFORM_IS_ROW_MAJOR: float = None

GL_UNIFORM_MATRIX_STRIDE: float = None

GL_UNIFORM_NAME_LENGTH: float = None

GL_UNIFORM_OFFSET: float = None

GL_UNIFORM_SIZE: float = None

GL_UNIFORM_TYPE: float = None

GL_UNPACK_ALIGNMENT: float = None

GL_UNPACK_IMAGE_HEIGHT: float = None

GL_UNPACK_LSB_FIRST: float = None

GL_UNPACK_ROW_LENGTH: float = None

GL_UNPACK_SKIP_IMAGES: float = None

GL_UNPACK_SKIP_PIXELS: float = None

GL_UNPACK_SKIP_ROWS: float = None

GL_UNPACK_SWAP_BYTES: float = None

GL_UNSIGNALED: float = None

GL_UNSIGNED_BYTE: float = None

GL_UNSIGNED_BYTE_2_3_3_REV: float = None

GL_UNSIGNED_BYTE_3_3_2: float = None

GL_UNSIGNED_INT: float = None

GL_UNSIGNED_INT_10F_11F_11F_REV: float = None

GL_UNSIGNED_INT_10_10_10_2: float = None

GL_UNSIGNED_INT_24_8: float = None

GL_UNSIGNED_INT_2_10_10_10_REV: float = None

GL_UNSIGNED_INT_5_9_9_9_REV: float = None

GL_UNSIGNED_INT_8_8_8_8: float = None

GL_UNSIGNED_INT_8_8_8_8_REV: float = None

GL_UNSIGNED_INT_SAMPLER_1D: float = None

GL_UNSIGNED_INT_SAMPLER_1D_ARRAY: float = None

GL_UNSIGNED_INT_SAMPLER_2D: float = None

GL_UNSIGNED_INT_SAMPLER_2D_ARRAY: float = None

GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE: float = None

GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY: float = None

GL_UNSIGNED_INT_SAMPLER_2D_RECT: float = None

GL_UNSIGNED_INT_SAMPLER_3D: float = None

GL_UNSIGNED_INT_SAMPLER_BUFFER: float = None

GL_UNSIGNED_INT_SAMPLER_CUBE: float = None

GL_UNSIGNED_INT_VEC2: float = None

GL_UNSIGNED_INT_VEC3: float = None

GL_UNSIGNED_INT_VEC4: float = None

GL_UNSIGNED_NORMALIZED: float = None

GL_UNSIGNED_SHORT: float = None

GL_UNSIGNED_SHORT_1_5_5_5_REV: float = None

GL_UNSIGNED_SHORT_4_4_4_4: float = None

GL_UNSIGNED_SHORT_4_4_4_4_REV: float = None

GL_UNSIGNED_SHORT_5_5_5_1: float = None

GL_UNSIGNED_SHORT_5_6_5: float = None

GL_UNSIGNED_SHORT_5_6_5_REV: float = None

GL_UPPER_LEFT: float = None

GL_VALIDATE_STATUS: float = None

GL_VENDOR: float = None

GL_VERSION: float = None

GL_VERTEX_ARRAY_BINDING: float = None

GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING: float = None

GL_VERTEX_ATTRIB_ARRAY_DIVISOR: float = None

GL_VERTEX_ATTRIB_ARRAY_ENABLED: float = None

GL_VERTEX_ATTRIB_ARRAY_INTEGER: float = None

GL_VERTEX_ATTRIB_ARRAY_NORMALIZED: float = None

GL_VERTEX_ATTRIB_ARRAY_POINTER: float = None

GL_VERTEX_ATTRIB_ARRAY_SIZE: float = None

GL_VERTEX_ATTRIB_ARRAY_STRIDE: float = None

GL_VERTEX_ATTRIB_ARRAY_TYPE: float = None

GL_VERTEX_PROGRAM_POINT_SIZE: float = None

GL_VERTEX_SHADER: float = None

GL_VIEWPORT: float = None

GL_WAIT_FAILED: float = None

GL_WRITE_ONLY: float = None

GL_XOR: float = None

GL_ZERO: float = None


def ActiveTexture(p0: int):
    '''

    :type p0: int
    '''

    pass


def AttachShader(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def BeginQuery(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def BindAttribLocation(p0: int, p1: int, p2: str):
    '''

    :type p0: int
    :type p1: int
    :type p2: str
    '''

    pass


def BindBuffer(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def BindBufferBase(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def BindBufferRange(p0: int, p1: int, p2: int, p3: int, p4: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    '''

    pass


def BindFramebuffer(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def BindRenderbuffer(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def BindTexture(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def BindVertexArray(p0: int):
    '''

    :type p0: int
    '''

    pass


def BlendColor(p0: float, p1: float, p2: float, p3: float):
    '''

    :type p0: float
    :type p1: float
    :type p2: float
    :type p3: float
    '''

    pass


def BlendEquation(p0: int):
    '''

    :type p0: int
    '''

    pass


def BlendEquationSeparate(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def BlendFunc(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def BlitFramebuffer(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                    p6: int, p7: int, p8: int, p9: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    :type p8: int
    :type p9: int
    '''

    pass


def BufferData(p0: int, p1: int, p2, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p3: int
    '''

    pass


def BufferSubData(p0: int, p1: int, p2: int, p3):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def CheckFramebufferStatus(p0: int) -> int:
    '''

    :type p0: int
    '''

    pass


def Clear(p0: int):
    '''

    :type p0: int
    '''

    pass


def ClearColor(p0: float, p1: float, p2: float, p3: float):
    '''

    :type p0: float
    :type p1: float
    :type p2: float
    :type p3: float
    '''

    pass


def ClearDepth(p0: float):
    '''

    :type p0: float
    '''

    pass


def ClearStencil(p0: int):
    '''

    :type p0: int
    '''

    pass


def ColorMask(p0: bool, p1: bool, p2: bool, p3: bool):
    '''

    :type p0: bool
    :type p1: bool
    :type p2: bool
    :type p3: bool
    '''

    pass


def CompileShader(p0: int):
    '''

    :type p0: int
    '''

    pass


def CompressedTexImage1D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                         p6):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    '''

    pass


def CompressedTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                         p6: int, p7):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    '''

    pass


def CompressedTexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                         p6: int, p7: int, p8):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    '''

    pass


def CompressedTexSubImage1D(p0: int, p1: int, p2: int, p3: int, p4: int,
                            p5: int, p6):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    '''

    pass


def CompressedTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int,
                            p5: int, p6: int, p7: int, p8):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    '''

    pass


def CopyTexImage1D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                   p6: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    '''

    pass


def CopyTexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                   p6: int, p7: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    '''

    pass


def CopyTexSubImage1D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    '''

    pass


def CopyTexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                      p6: int, p7: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    '''

    pass


def CopyTexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                      p6: int, p7: int, p8: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    :type p8: int
    '''

    pass


def CreateProgram(p0) -> int:
    '''

    '''

    pass


def CreateShader(p0: int) -> int:
    '''

    :type p0: int
    '''

    pass


def CullFace(p0: int):
    '''

    :type p0: int
    '''

    pass


def DeleteBuffers(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def DeleteFramebuffers(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def DeleteProgram(p0: int):
    '''

    :type p0: int
    '''

    pass


def DeleteQueries(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def DeleteRenderbuffers(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def DeleteShader(p0: int):
    '''

    :type p0: int
    '''

    pass


def DeleteTextures(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def DeleteVertexArrays(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def DepthFunc(p0: int):
    '''

    :type p0: int
    '''

    pass


def DepthMask(p0: bool):
    '''

    :type p0: bool
    '''

    pass


def DepthRange(p0: float, p1: float):
    '''

    :type p0: float
    :type p1: float
    '''

    pass


def DetachShader(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def Disable(p0: int):
    '''

    :type p0: int
    '''

    pass


def DisableVertexAttribArray(p0: int):
    '''

    :type p0: int
    '''

    pass


def DrawArrays(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def DrawBuffer(p0: int):
    '''

    :type p0: int
    '''

    pass


def DrawBuffers(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def DrawElements(p0: int, p1: int, p2: int, p3):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def DrawRangeElements(p0: int, p1: int, p2: int, p3: int, p4: int, p5):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    '''

    pass


def Enable(p0: int):
    '''

    :type p0: int
    '''

    pass


def EnableVertexAttribArray(p0: int):
    '''

    :type p0: int
    '''

    pass


def EndQuery(p0: int):
    '''

    :type p0: int
    '''

    pass


def Finish(p0):
    '''

    '''

    pass


def Flush(p0):
    '''

    '''

    pass


def FramebufferRenderbuffer(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def FramebufferTexture(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def FrontFace(p0: int):
    '''

    :type p0: int
    '''

    pass


def GenBuffers(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GenFramebuffers(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GenQueries(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GenRenderbuffers(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GenTextures(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GenVertexArrays(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GetActiveAttrib(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                    p6: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    '''

    pass


def GetActiveUniform(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                     p6: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    '''

    pass


def GetActiveUniformBlockName(p0: int, p1: int, p2: int, p3: int, p4: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    '''

    pass


def GetActiveUniformBlockiv(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def GetActiveUniformName(p0: int, p1: int, p2: int, p3: int, p4: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    '''

    pass


def GetActiveUniformsiv(p0: int, p1: int, p2: int, p3: int, p4: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    '''

    pass


def GetAttachedShaders(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def GetAttribLocation(p0: int, p1: str) -> int:
    '''

    :type p0: int
    :type p1: str
    '''

    pass


def GetBooleanv(p0: int, p1: bool):
    '''

    :type p0: int
    :type p1: bool
    '''

    pass


def GetBufferParameteri64v(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetBufferParameteriv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetBufferPointerv(p0: int, p1: int, p2):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GetBufferSubData(p0: int, p1: int, p2: int, p3):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetCompressedTexImage(p0: int, p1: int, p2):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GetDoublev(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def GetError(p0) -> int:
    '''

    '''

    pass


def GetFloatv(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def GetIntegerv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GetMultisamplefv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def GetProgramInfoLog(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def GetProgramiv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetQueryObjectiv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetQueryObjectuiv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetQueryiv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetShaderInfoLog(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def GetShaderSource(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def GetShaderiv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetString(p0: int) -> str:
    '''

    :type p0: int
    '''

    pass


def GetStringi(p0: int, p1: int) -> str:
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GetTexImage(p0: int, p1: int, p2: int, p3: int, p4):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def GetTexLevelParameterfv(p0: int, p1: int, p2: int, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: float
    '''

    pass


def GetTexLevelParameteriv(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def GetTexParameterfv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def GetTexParameteriv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetUniformBlockIndex(p0: int, p1: str) -> int:
    '''

    :type p0: int
    :type p1: str
    '''

    pass


def GetUniformIndices(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def GetUniformLocation(p0: int, p1: str) -> int:
    '''

    :type p0: int
    :type p1: str
    '''

    pass


def GetUniformfv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def GetUniformiv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def GetVertexAttribPointerv(p0: int, p1: int, p2):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def GetVertexAttribdv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def GetVertexAttribfv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def GetVertexAttribiv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def Hint(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def IsBuffer(p0: int) -> bool:
    '''

    :type p0: int
    '''

    pass


def IsEnabled(p0: int) -> bool:
    '''

    :type p0: int
    '''

    pass


def IsProgram(p0: int) -> bool:
    '''

    :type p0: int
    '''

    pass


def IsQuery(p0: int) -> bool:
    '''

    :type p0: int
    '''

    pass


def IsShader(p0: int) -> bool:
    '''

    :type p0: int
    '''

    pass


def IsTexture(p0: int) -> bool:
    '''

    :type p0: int
    '''

    pass


def IsVertexArray(p0: int) -> bool:
    '''

    :type p0: int
    '''

    pass


def LineWidth(p0: float):
    '''

    :type p0: float
    '''

    pass


def LinkProgram(p0: int):
    '''

    :type p0: int
    '''

    pass


def LogicOp(p0: int):
    '''

    :type p0: int
    '''

    pass


def MapBuffer(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def PixelStoref(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def PixelStorei(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def PointSize(p0: float):
    '''

    :type p0: float
    '''

    pass


def PolygonMode(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def PolygonOffset(p0: float, p1: float):
    '''

    :type p0: float
    :type p1: float
    '''

    pass


def ReadBuffer(p0: int):
    '''

    :type p0: int
    '''

    pass


def ReadPixels(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    '''

    pass


def RenderbufferStorage(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def SampleCoverage(p0: float, p1: bool):
    '''

    :type p0: float
    :type p1: bool
    '''

    pass


def SampleMaski(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def Scissor(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def StencilFunc(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def StencilFuncSeparate(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def StencilMask(p0: int):
    '''

    :type p0: int
    '''

    pass


def StencilMaskSeparate(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def StencilOp(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def StencilOpSeparate(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def TexImage1D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int,
               p7):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    '''

    pass


def TexImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int,
               p7: int, p8):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    '''

    pass


def TexImage2DMultisample(p0: int, p1: int, p2: int, p3: int, p4: int,
                          p5: bool):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: bool
    '''

    pass


def TexImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6: int,
               p7: int, p8: int, p9):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    :type p8: int
    '''

    pass


def TexImage3DMultisample(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                          p6: bool):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: bool
    '''

    pass


def TexParameterf(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def TexParameterfv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def TexParameteri(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def TexParameteriv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def TexSubImage1D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int, p6):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    '''

    pass


def TexSubImage2D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                  p6: int, p7: int, p8):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    '''

    pass


def TexSubImage3D(p0: int, p1: int, p2: int, p3: int, p4: int, p5: int,
                  p6: int, p7: int, p8: int, p9: int, p10):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    :type p5: int
    :type p6: int
    :type p7: int
    :type p8: int
    :type p9: int
    '''

    pass


def Uniform1f(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def Uniform1fv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def Uniform1i(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def Uniform1iv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def Uniform2f(p0: int, p1: float, p2: float):
    '''

    :type p0: int
    :type p1: float
    :type p2: float
    '''

    pass


def Uniform2fv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def Uniform2i(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def Uniform2iv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def Uniform3f(p0: int, p1: float, p2: float, p3: float):
    '''

    :type p0: int
    :type p1: float
    :type p2: float
    :type p3: float
    '''

    pass


def Uniform3fv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def Uniform3i(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def Uniform3iv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def Uniform4f(p0: int, p1: float, p2: float, p3: float, p4: float):
    '''

    :type p0: int
    :type p1: float
    :type p2: float
    :type p3: float
    :type p4: float
    '''

    pass


def Uniform4fv(p0: int, p1: int, p2: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: float
    '''

    pass


def Uniform4i(p0: int, p1: int, p2: int, p3: int, p4: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    '''

    pass


def Uniform4iv(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def UniformBlockBinding(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def UniformMatrix2fv(p0: int, p1: int, p2: bool, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: bool
    :type p3: float
    '''

    pass


def UniformMatrix2x3fv(p0: int, p1: int, p2: bool, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: bool
    :type p3: float
    '''

    pass


def UniformMatrix2x4fv(p0: int, p1: int, p2: bool, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: bool
    :type p3: float
    '''

    pass


def UniformMatrix3fv(p0: int, p1: int, p2: bool, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: bool
    :type p3: float
    '''

    pass


def UniformMatrix3x2fv(p0: int, p1: int, p2: bool, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: bool
    :type p3: float
    '''

    pass


def UniformMatrix3x4fv(p0: int, p1: int, p2: bool, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: bool
    :type p3: float
    '''

    pass


def UniformMatrix4fv(p0: int, p1: int, p2: bool, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: bool
    :type p3: float
    '''

    pass


def UniformMatrix4x2fv(p0: int, p1: int, p2: bool, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: bool
    :type p3: float
    '''

    pass


def UniformMatrix4x3fv(p0: int, p1: int, p2: bool, p3: float):
    '''

    :type p0: int
    :type p1: int
    :type p2: bool
    :type p3: float
    '''

    pass


def UnmapBuffer(p0: int) -> bool:
    '''

    :type p0: int
    '''

    pass


def UseProgram(p0: int):
    '''

    :type p0: int
    '''

    pass


def ValidateProgram(p0: int):
    '''

    :type p0: int
    '''

    pass


def VertexAttrib1d(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib1dv(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib1f(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib1fv(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib1s(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib1sv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib2d(p0: int, p1: float, p2: float):
    '''

    :type p0: int
    :type p1: float
    :type p2: float
    '''

    pass


def VertexAttrib2dv(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib2f(p0: int, p1: float, p2: float):
    '''

    :type p0: int
    :type p1: float
    :type p2: float
    '''

    pass


def VertexAttrib2fv(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib2s(p0: int, p1: int, p2: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    '''

    pass


def VertexAttrib2sv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib3d(p0: int, p1: float, p2: float, p3: float):
    '''

    :type p0: int
    :type p1: float
    :type p2: float
    :type p3: float
    '''

    pass


def VertexAttrib3dv(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib3f(p0: int, p1: float, p2: float, p3: float):
    '''

    :type p0: int
    :type p1: float
    :type p2: float
    :type p3: float
    '''

    pass


def VertexAttrib3fv(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib3s(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def VertexAttrib3sv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4Nbv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4Niv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4Nsv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4Nub(p0: int, p1: int, p2: int, p3: int, p4: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    '''

    pass


def VertexAttrib4Nubv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4Nuiv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4Nusv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4bv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4d(p0: int, p1: float, p2: float, p3: float, p4: float):
    '''

    :type p0: int
    :type p1: float
    :type p2: float
    :type p3: float
    :type p4: float
    '''

    pass


def VertexAttrib4dv(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib4f(p0: int, p1: float, p2: float, p3: float, p4: float):
    '''

    :type p0: int
    :type p1: float
    :type p2: float
    :type p3: float
    :type p4: float
    '''

    pass


def VertexAttrib4fv(p0: int, p1: float):
    '''

    :type p0: int
    :type p1: float
    '''

    pass


def VertexAttrib4iv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4s(p0: int, p1: int, p2: int, p3: int, p4: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    :type p4: int
    '''

    pass


def VertexAttrib4sv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4ubv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4uiv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttrib4usv(p0: int, p1: int):
    '''

    :type p0: int
    :type p1: int
    '''

    pass


def VertexAttribPointer(p0: int, p1: int, p2: int, p3: bool, p4: int, p5):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: bool
    :type p4: int
    '''

    pass


def Viewport(p0: int, p1: int, p2: int, p3: int):
    '''

    :type p0: int
    :type p1: int
    :type p2: int
    :type p3: int
    '''

    pass


def glAccum(op: typing.Union[int, str], value: float):
    '''Operate on the accumulation buffer. 

    :param op: The accumulation buffer operation. 
    :type op: typing.Union[int, str]
    :param value: a value used in the accumulation buffer operation. 
    :type value: float
    '''

    pass


def glActiveTexture(texture: int):
    '''Select active texture unit. 

    :param texture: Constant in GL_TEXTURE0 0 - 8 
    :type texture: int
    '''

    pass


def glAlphaFunc(func: typing.Union[int, str], ref: float):
    '''Specify the alpha test function. 

    :param func: Specifies the alpha comparison function. 
    :type func: typing.Union[int, str]
    :param ref: The reference value that incoming alpha values are compared to. Clamped between 0 and 1. 
    :type ref: float
    '''

    pass


def glAreTexturesResident(n: int, textures: 'bpy.context.object',
                          residences: bool):
    '''Determine if textures are loaded in texture memory 

    :param n: Specifies the number of textures to be queried. 
    :type n: int
    :param textures: Specifies an array containing the names of the textures to be queried 
    :type textures: 'bpy.context.object'
    :param residences: An array in which the texture residence status in returned. The residence status of a texture named by an element of textures is returned in the corresponding element of residences. 
    :type residences: bool
    '''

    pass


def glAttachShader(program: int, shader: int):
    '''Attaches a shader object to a program object. 

    :param program: Specifies the program object to which a shader object will be attached. 
    :type program: int
    :param shader: Specifies the shader object that is to be attached. 
    :type shader: int
    '''

    pass


def glBegin(mode: typing.Union[int, str]):
    '''Delimit the vertices of a primitive or a group of like primatives 

    :param mode: Specifies the primitive that will be create from vertices between glBegin and glEnd. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glBindTexture(target: typing.Union[int, str], texture: int):
    '''Bind a named texture to a texturing target 

    :param target: Specifies the target to which the texture is bound. 
    :type target: typing.Union[int, str]
    :param texture: Specifies the name of a texture. 
    :type texture: int
    '''

    pass


def glBitmap(width, height, xorig, yorig, xmove, ymove,
             bitmap: 'bpy.context.object'):
    '''Draw a bitmap 

    :param height: Specify the pixel width and height of the bitmap image. 
    :param yorig: Specify the location of the origin in the bitmap image. The origin is measured from the lower left corner of the bitmap, with right and up being the positive axes. 
    :param ymove: Specify the x and y offsets to be added to the current raster position after the bitmap is drawn. 
    :param bitmap: Specifies the address of the bitmap image. 
    :type bitmap: 'bpy.context.object'
    '''

    pass


def glBlendFunc(sfactor: typing.Union[int, str],
                dfactor: typing.Union[int, str]):
    '''Specify pixel arithmetic 

    :param sfactor: Specifies how the red, green, blue, and alpha source blending factors are computed. 
    :type sfactor: typing.Union[int, str]
    :param dfactor: Specifies how the red, green, blue, and alpha destination blending factors are computed. 
    :type dfactor: typing.Union[int, str]
    '''

    pass


def glCallList(list: int):
    '''Execute a display list 

    :param list: Specifies the integer name of the display list to be executed. 
    :type list: int
    '''

    pass


def glCallLists(n: int, type: typing.Union[int, str],
                lists: 'bpy.context.object'):
    '''Execute a list of display lists 

    :param n: Specifies the number of display lists to be executed. 
    :type n: int
    :param type: Specifies the type of values in lists. 
    :type type: typing.Union[int, str]
    :param lists: Specifies the address of an array of name offsets in the display list. The pointer type is void because the offsets can be bytes, shorts, ints, or floats, depending on the value of type. 
    :type lists: 'bpy.context.object'
    '''

    pass


def glClear(mask):
    '''Clear buffers to preset values 

    :param mask: Bitwise OR of masks that indicate the buffers to be cleared. 
    '''

    pass


def glClearAccum(red, green, blue, alpha):
    '''Specify clear values for the accumulation buffer 

    :param alpha: Specify the red, green, blue, and alpha values used when the accumulation buffer is cleared. The initial values are all 0. 
    '''

    pass


def glClearColor(red, green, blue, alpha):
    '''Specify clear values for the color buffers 

    :param alpha: Specify the red, green, blue, and alpha values used when the color buffers are cleared. The initial values are all 0. 
    '''

    pass


def glClearDepth(depth: int):
    '''Specify the clear value for the depth buffer 

    :param depth: Specifies the depth value used when the depth buffer is cleared. The initial value is 1. 
    :type depth: int
    '''

    pass


def glClearIndex(c: float):
    '''Specify the clear value for the color index buffers 

    :param c: Specifies the index used when the color index buffers are cleared. The initial value is 0. 
    :type c: float
    '''

    pass


def glClearStencil(s: int):
    '''Specify the clear value for the stencil buffer 

    :param s: Specifies the index used when the stencil buffer is cleared. The initial value is 0. 
    :type s: int
    '''

    pass


def glClipPlane(plane: typing.Union[int, str], equation: 'bpy.context.object'):
    '''Specify a plane against which all geometry is clipped 

    :param plane: Specifies which clipping plane is being positioned. 
    :type plane: typing.Union[int, str]
    :param equation: Specifies the address of an array of four double- precision floating-point values. These values are interpreted as a plane equation. 
    :type equation: 'bpy.context.object'
    '''

    pass


def glColor(red, green, blue, alpha):
    '''Set a new color. 

    :param blue: Specify new red, green, and blue values for the current color. 
    :param alpha: Specifies a new alpha value for the current color. Included only in the four-argument glColor4 commands. (With '4' colors only) 
    '''

    pass


def glColorMask(red, green, blue, alpha):
    '''Enable and disable writing of frame buffer color components 

    :param alpha: Specify whether red, green, blue, and alpha can or cannot be written into the frame buffer. The initial values are all GL_TRUE, indicating that the color components can be written. 
    '''

    pass


def glColorMaterial(face: typing.Union[int, str],
                    mode: typing.Union[int, str]):
    '''Cause a material color to track the current color 

    :param face: Specifies whether front, back, or both front and back material parameters should track the current color. 
    :type face: typing.Union[int, str]
    :param mode: Specifies which of several material parameters track the current color. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glCompileShader(shader: int):
    '''Compiles a shader object. 

    :param shader: Specifies the shader object to be compiled. 
    :type shader: int
    '''

    pass


def glCopyPixels(x, y, width: int, height: int, type):
    '''Copy pixels into a 2D texture image 

    :param target: Specifies the target texture. 
    :type target: typing.Union[int, str]
    :param level: Specifies the level-of-detail number. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param internalformat: Specifies the number of color components in the texture. 
    :type internalformat: int
    :param y: Specify the window coordinates of the first pixel that is copied from the frame buffer. This location is the lower left corner of a rectangular block of pixels. 
    :param width: Specifies the width of the texture image. Must be 2n+2(border) for some integer n. All implementations support texture images that are at least 64 texels wide. 
    :type width: int
    :param height: Specifies the height of the texture image. Must be 2m+2(border) for some integer m. All implementations support texture images that are at least 64 texels high. 
    :type height: int
    :param border: Specifies the width of the border. Must be either 0 or 1. 
    :type border: int
    '''

    pass


def glCreateProgram() -> int:
    '''Creates a program object 

    :return:  The new program or zero if an error occurs. 
    '''

    pass


def glCreateShader(shaderType: 'GL_VERTEX_SHADER') -> int:
    '''Creates a shader object. 

    :type shaderType: 'GL_VERTEX_SHADER'
    :return:  0 if an error occurs. 
    '''

    pass


def glCullFace(mode: typing.Union[int, str]):
    '''Specify whether front- or back-facing facets can be culled 

    :param mode: Specifies whether front- or back-facing facets are candidates for culling. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glDeleteLists(list: int, range: int):
    '''Delete a contiguous group of display lists 

    :param list: Specifies the integer name of the first display list to delete 
    :type list: int
    :param range: Specifies the number of display lists to delete 
    :type range: int
    '''

    pass


def glDeleteProgram(program: int):
    '''Deletes a program object. 

    :param program: Specifies the program object to be deleted. 
    :type program: int
    '''

    pass


def glDeleteShader(shader: int):
    '''Deletes a shader object. 

    :param shader: Specifies the shader object to be deleted. 
    :type shader: int
    '''

    pass


def glDeleteTextures(n: int, textures: 'Buffer'):
    '''Delete named textures 

    :param n: Specifies the number of textures to be deleted 
    :type n: int
    :param textures: Specifies an array of textures to be deleted 
    :type textures: 'Buffer'
    '''

    pass


def glDepthFunc(func: typing.Union[int, str]):
    '''Specify the value used for depth buffer comparisons 

    :param func: Specifies the depth comparison function. 
    :type func: typing.Union[int, str]
    '''

    pass


def glDepthMask(flag: typing.Union[int, bool]):
    '''Enable or disable writing into the depth buffer 

    :param flag: Specifies whether the depth buffer is enabled for writing. If flag is GL_FALSE, depth buffer writing is disabled. Otherwise, it is enabled. Initially, depth buffer writing is enabled. 
    :type flag: typing.Union[int, bool]
    '''

    pass


def glDepthRange(zNear: int, zFar: int):
    '''Specify mapping of depth values from normalized device coordinates to window coordinates 

    :param zNear: Specifies the mapping of the near clipping plane to window coordinates. The initial value is 0. 
    :type zNear: int
    :param zFar: Specifies the mapping of the far clipping plane to window coordinates. The initial value is 1. 
    :type zFar: int
    '''

    pass


def glDetachShader(program: int, shader: int):
    '''Detaches a shader object from a program object to which it is attached. 

    :param program: Specifies the program object from which to detach the shader object. 
    :type program: int
    :param shader: pecifies the program object from which to detach the shader object. 
    :type shader: int
    '''

    pass


def glDisable(cap: typing.Union[int, str]):
    '''Disable server-side GL capabilities 

    :param cap: Specifies a symbolic constant indicating a GL capability. 
    :type cap: typing.Union[int, str]
    '''

    pass


def glDrawBuffer(mode: typing.Union[int, str]):
    '''Specify which color buffers are to be drawn into 

    :param mode: Specifies up to four color buffers to be drawn into. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glDrawPixels(width, height, format: typing.Union[int, str],
                 type: typing.Union[int, str], pixels: 'bpy.context.object'):
    '''Write a block of pixels to the frame buffer 

    :param height: Specify the dimensions of the pixel rectangle to be written into the frame buffer. 
    :param format: Specifies the format of the pixel data. 
    :type format: typing.Union[int, str]
    :param type: Specifies the data type for pixels. 
    :type type: typing.Union[int, str]
    :param pixels: Specifies a pointer to the pixel data. 
    :type pixels: 'bpy.context.object'
    '''

    pass


def glEdgeFlag(flag):
    '''Flag edges as either boundary or non-boundary 

    :param flag: Specifies the current edge flag value.The initial value is GL_TRUE. 
    '''

    pass


def glEnable(cap: typing.Union[int, str]):
    '''Enable server-side GL capabilities 

    :param cap: Specifies a symbolic constant indicating a GL capability. 
    :type cap: typing.Union[int, str]
    '''

    pass


def glEnd():
    '''Delimit the vertices of a primitive or group of like primitives 

    '''

    pass


def glEndList():
    '''Create or replace a display list 

    '''

    pass


def glEvalCoord(u, v):
    '''Evaluate enabled one- and two-dimensional maps 

    :param u: Specifies a value that is the domain coordinate u to the basis function defined in a previous glMap1 or glMap2 command. If the function prototype ends in 'v' then u specifies a pointer to an array containing either one or two domain coordinates. The first coordinate is u. The second coordinate is v, which is present only in glEvalCoord2 versions. 
    :param v: Specifies a value that is the domain coordinate v to the basis function defined in a previous glMap2 command. This argument is not present in a glEvalCoord1 command. 
    '''

    pass


def glEvalMesh(mode: typing.Union[int, str], i1, i2):
    '''Compute a one- or two-dimensional grid of points or lines 

    :param mode: In glEvalMesh1, specifies whether to compute a one-dimensional mesh of points or lines. 
    :type mode: typing.Union[int, str]
    :param i2: Specify the first and last integer values for the grid domain variable i. 
    '''

    pass


def glEvalPoint(i: int, j: int):
    '''Generate and evaluate a single point in a mesh 

    :param i: Specifies the integer value for grid domain variable i. 
    :type i: int
    :param j: Specifies the integer value for grid domain variable j (glEvalPoint2 only). 
    :type j: int
    '''

    pass


def glFeedbackBuffer(size: int, type: typing.Union[int, str],
                     buffer: 'bpy.context.object'):
    '''Controls feedback mode 

    :param size: Specifies the maximum number of values that can be written into buffer. 
    :type size: int
    :param type: Specifies a symbolic constant that describes the information that will be returned for each vertex. 
    :type type: typing.Union[int, str]
    :param buffer: Returns the feedback data. 
    :type buffer: 'bpy.context.object'
    '''

    pass


def glFinish():
    '''Block until all GL execution is complete 

    '''

    pass


def glFlush():
    '''Force Execution of GL commands in finite time 

    '''

    pass


def glFog(pname: typing.Union[int, str], param):
    '''Specify fog parameters 

    :param pname: Specifies a single-valued fog parameter. If the function prototype ends in 'v' specifies a fog parameter. 
    :type pname: typing.Union[int, str]
    :param param: Specifies the value or values to be assigned to pname. GL_FOG_COLOR requires an array of four values. All other parameters accept an array containing only a single value. 
    '''

    pass


def glFrontFace(mode: typing.Union[int, str]):
    '''Define front- and back-facing polygons 

    :param mode: Specifies the orientation of front-facing polygons. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glFrustum(left, right, bottom, top, zNear, zFar):
    '''Multiply the current matrix by a perspective matrix 

    :param right: Specify the coordinates for the left and right vertical clipping planes. 
    :param bottom: Specify the coordinates for the bottom and top horizontal clipping planes. 
    :param zFar: Specify the distances to the near and far depth clipping planes. Both distances must be positive. 
    '''

    pass


def glGenLists(range: int):
    '''Generate a contiguous set of empty display lists 

    :param range: Specifies the number of contiguous empty display lists to be generated. 
    :type range: int
    '''

    pass


def glGenTextures(n: int, textures: 'bpy.context.object'):
    '''Generate texture names 

    :param n: Specifies the number of textures name to be generated. 
    :type n: int
    :param textures: Specifies an array in which the generated textures names are stored. 
    :type textures: 'bpy.context.object'
    '''

    pass


def glGet(pname: typing.Union[int, str], param):
    '''Return the value or values of a selected parameter 

    :param pname: Specifies the parameter value to be returned. 
    :type pname: typing.Union[int, str]
    :param param: Returns the value or values of the specified parameter. 
    '''

    pass


def glGetAttachedShaders(program: int, maxCount: int, count: int,
                         shaders: int):
    '''Returns the handles of the shader objects attached to a program object. 

    :param program: Specifies the program object to be queried. 
    :type program: int
    :param maxCount: Specifies the size of the array for storing the returned object names. 
    :type maxCount: int
    :param count: Returns the number of names actually returned in objects. 
    :type count: int
    :param shaders: Specifies an array that is used to return the names of attached shader objects. 
    :type shaders: int
    '''

    pass


def glGetClipPlane(plane: typing.Union[int, str],
                   equation: 'bpy.context.object'):
    '''Return the coefficients of the specified clipping plane 

    :param plane: Specifies a clipping plane. The number of clipping planes depends on the implementation, but at least six clipping planes are supported. They are identified by symbolic names of the form GL_CLIP_PLANEi where 0 < i < GL_MAX_CLIP_PLANES. 
    :type plane: typing.Union[int, str]
    :param equation: Returns four float (double)-precision values that are the coefficients of the plane equation of plane in eye coordinates. The initial value is (0, 0, 0, 0). 
    :type equation: 'bpy.context.object'
    '''

    pass


def glGetError():
    '''Return error information 

    '''

    pass


def glGetLight(light: typing.Union[int, str], pname: typing.Union[int, str],
               params: 'Buffer'):
    '''Return light source parameter values 

    :param light: Specifies a light source. The number of possible lights depends on the implementation, but at least eight lights are supported. They are identified by symbolic names of the form GL_LIGHTi where 0 < i < GL_MAX_LIGHTS. 
    :type light: typing.Union[int, str]
    :param pname: Specifies a light source parameter for light. 
    :type pname: typing.Union[int, str]
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetMap(target: typing.Union[int, str], query: typing.Union[int, str],
             v: 'Buffer'):
    '''Return evaluator parameters 

    :param target: Specifies the symbolic name of a map. 
    :type target: typing.Union[int, str]
    :param query: Specifies which parameter to return. 
    :type query: typing.Union[int, str]
    :param v: Returns the requested data. 
    :type v: 'Buffer'
    '''

    pass


def glGetMaterial(face: typing.Union[int, str], pname: typing.Union[int, str],
                  params: 'Buffer'):
    '''Return material parameters 

    :param face: Specifies which of the two materials is being queried. representing the front and back materials, respectively. 
    :type face: typing.Union[int, str]
    :param pname: Specifies the material parameter to return. 
    :type pname: typing.Union[int, str]
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetPixelMap(map: typing.Union[int, str], values: 'Buffer'):
    '''Return the specified pixel map 

    :param map: Specifies the name of the pixel map to return. 
    :type map: typing.Union[int, str]
    :param values: Returns the pixel map contents. 
    :type values: 'Buffer'
    '''

    pass


def glGetPolygonStipple(mask: 'bpy.context.object'):
    '''Return the polygon stipple pattern 

    :param mask: Returns the stipple pattern. The initial value is all 1's. 
    :type mask: 'bpy.context.object'
    '''

    pass


def glGetProgramInfoLog(program: int, maxLength: int, length: int,
                        infoLog: 'Buffer'):
    '''Returns the information log for a program object. 

    :param program: Specifies the program object whose information log is to be queried. 
    :type program: int
    :param maxLength: Specifies the size of the character buffer for storing the returned information log. 
    :type maxLength: int
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator). 
    :type length: int
    :param infoLog: Specifies an array of characters that is used to return the information log. 
    :type infoLog: 'Buffer'
    '''

    pass


def glGetProgramiv(program: int, pname: int, params: int):
    '''Returns a parameter from a program object. 

    :param program: Specifies the program object to be queried. 
    :type program: int
    :param pname: Specifies the object parameter. 
    :type pname: int
    :param params: Returns the requested object parameter. 
    :type params: int
    '''

    pass


def glGetShaderInfoLog(program, maxLength: int, length: int,
                       infoLog: 'Buffer'):
    '''Returns the information log for a shader object. 

    :param shader: Specifies the shader object whose information log is to be queried. 
    :type shader: int
    :param maxLength: Specifies the size of the character buffer for storing the returned information log. 
    :type maxLength: int
    :param length: Returns the length of the string returned in infoLog (excluding the null terminator). 
    :type length: int
    :param infoLog: Specifies an array of characters that is used to return the information log. 
    :type infoLog: 'Buffer'
    '''

    pass


def glGetShaderSource(shader: int, bufSize: int, length: int,
                      source: 'Buffer'):
    '''Returns the source code string from a shader object 

    :param shader: Specifies the shader object to be queried. 
    :type shader: int
    :param bufSize: Specifies the size of the character buffer for storing the returned source code string. 
    :type bufSize: int
    :param length: Returns the length of the string returned in source (excluding the null terminator). 
    :type length: int
    :param source: Specifies an array of characters that is used to return the source code string. 
    :type source: 'Buffer'
    '''

    pass


def glGetString(name: typing.Union[int, str]):
    '''Return a string describing the current GL connection 

    :param name: Specifies a symbolic constant. 
    :type name: typing.Union[int, str]
    '''

    pass


def glGetTexEnv(target: typing.Union[int, str], pname: typing.Union[int, str],
                params: 'Buffer'):
    '''Return texture environment parameters 

    :param target: Specifies a texture environment. Must be GL_TEXTURE_ENV. 
    :type target: typing.Union[int, str]
    :param pname: Specifies the symbolic name of a texture environment parameter. 
    :type pname: typing.Union[int, str]
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetTexGen(coord: typing.Union[int, str], pname: typing.Union[int, str],
                params: 'Buffer'):
    '''Return texture coordinate generation parameters 

    :param coord: Specifies a texture coordinate. 
    :type coord: typing.Union[int, str]
    :param pname: Specifies the symbolic name of the value(s) to be returned. 
    :type pname: typing.Union[int, str]
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetTexImage(target: typing.Union[int, str], level: int,
                  format: typing.Union[int, str], type: typing.Union[int, str],
                  pixels: 'Buffer'):
    '''Return a texture image 

    :param target: Specifies which texture is to be obtained. 
    :type target: typing.Union[int, str]
    :param level: Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param format: Specifies a pixel format for the returned data. 
    :type format: typing.Union[int, str]
    :param type: Specifies a pixel type for the returned data. 
    :type type: typing.Union[int, str]
    :param pixels: Returns the texture image. Should be a pointer to an array of the type specified by type 
    :type pixels: 'Buffer'
    '''

    pass


def glGetTexLevelParameter(target: typing.Union[int, str], level: int,
                           pname: typing.Union[int, str], params: 'Buffer'):
    '''return texture parameter values for a specific level of detail 

    :param target: Specifies the symbolic name of the target texture. 
    :type target: typing.Union[int, str]
    :param level: Specifies the level-of-detail number of the desired image. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param pname: Specifies the symbolic name of a texture parameter. 
    :type pname: typing.Union[int, str]
    :param params: Returns the requested data. 
    :type params: 'Buffer'
    '''

    pass


def glGetTexParameter(target: typing.Union[int, str],
                      pname: typing.Union[int, str], params: 'Buffer'):
    '''Return texture parameter values 

    :param target: Specifies the symbolic name of the target texture. 
    :type target: typing.Union[int, str]
    :param pname: Specifies the symbolic name the target texture. 
    :type pname: typing.Union[int, str]
    :param params: Returns the texture parameters. 
    :type params: 'Buffer'
    '''

    pass


def glHint(target: typing.Union[int, str], mode: typing.Union[int, str]):
    '''Specify implementation-specific hints 

    :param target: Specifies a symbolic constant indicating the behavior to be controlled. 
    :type target: typing.Union[int, str]
    :param mode: Specifies a symbolic constant indicating the desired behavior. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glIndex(c: 'Buffer'):
    '''Set the current color index 

    :param c: Specifies a pointer to a one element array that contains the new value for the current color index. 
    :type c: 'Buffer'
    '''

    pass


def glIndexMask(mask: int):
    '''Control the writing of individual bits in the color index buffers 

    :param mask: Specifies a bit mask to enable and disable the writing of individual bits in the color index buffers. Initially, the mask is all 1's. 
    :type mask: int
    '''

    pass


def glInitNames():
    '''Initialize the name stack 

    '''

    pass


def glIsEnabled(cap: typing.Union[int, str]):
    '''Test whether a capability is enabled 

    :param cap: Specifies a constant representing a GL capability. 
    :type cap: typing.Union[int, str]
    '''

    pass


def glIsList(list: int):
    '''Determine if a name corresponds to a display-list 

    :param list: Specifies a potential display-list name. 
    :type list: int
    '''

    pass


def glIsProgram(program: int):
    '''Determines if a name corresponds to a program object 

    :param program: Specifies a potential program object. 
    :type program: int
    '''

    pass


def glIsShader(shader: int):
    '''Determines if a name corresponds to a shader object. 

    :param shader: Specifies a potential shader object. 
    :type shader: int
    '''

    pass


def glIsTexture(texture: int):
    '''Determine if a name corresponds to a texture 

    :param texture: Specifies a value that may be the name of a texture. 
    :type texture: int
    '''

    pass


def glLight(light: typing.Union[int, str], pname: typing.Union[int, str],
            param):
    '''Set the light source parameters 

    :param light: Specifies a light. The number of lights depends on the implementation, but at least eight lights are supported. They are identified by symbolic names of the form GL_LIGHTi where 0 < i < GL_MAX_LIGHTS. 
    :type light: typing.Union[int, str]
    :param pname: Specifies a single-valued light source parameter for light. 
    :type pname: typing.Union[int, str]
    :param param: Specifies the value that parameter pname of light source light will be set to. If function prototype ends in 'v' specifies a pointer to the value or values that parameter pname of light source light will be set to. 
    '''

    pass


def glLightModel(pname: typing.Union[int, str], param):
    '''Set the lighting model parameters 

    :param pname: Specifies a single-value light model parameter. 
    :type pname: typing.Union[int, str]
    :param param: Specifies the value that param will be set to. If function prototype ends in 'v' specifies a pointer to the value or values that param will be set to. 
    '''

    pass


def glLineStipple(factor: int, pattern: int):
    '''Specify the line stipple pattern 

    :param factor: Specifies a multiplier for each bit in the line stipple pattern. If factor is 3, for example, each bit in the pattern is used three times before the next bit in the pattern is used. factor is clamped to the range [1, 256] and defaults to 1. 
    :type factor: int
    :param pattern: Specifies a 16-bit integer whose bit pattern determines which fragments of a line will be drawn when the line is rasterized. Bit zero is used first; the default pattern is all 1's. 
    :type pattern: int
    '''

    pass


def glLineWidth(width: float):
    '''Specify the width of rasterized lines. 

    :param width: Specifies the width of rasterized lines. The initial value is 1. 
    :type width: float
    '''

    pass


def glLinkProgram(program: int):
    '''Links a program object. 

    :param program: Specifies the handle of the program object to be linked. 
    :type program: int
    '''

    pass


def glListBase(base: int):
    '''Set the display-list base for glCallLists 

    :param base: Specifies an integer offset that will be added to glCallLists offsets to generate display-list names. The initial value is 0. 
    :type base: int
    '''

    pass


def glLoadIdentity():
    '''Replace the current matrix with the identity matrix 

    '''

    pass


def glLoadMatrix(m: 'Buffer'):
    '''Replace the current matrix with the specified matrix 

    :param m: Specifies a pointer to 16 consecutive values, which are used as the elements of a 4x4 column-major matrix. 
    :type m: 'Buffer'
    '''

    pass


def glLoadName(name: int):
    '''Load a name onto the name stack. 

    :param name: Specifies a name that will replace the top value on the name stack. 
    :type name: int
    '''

    pass


def glLogicOp(opcode: typing.Union[int, str]):
    '''Specify a logical pixel operation for color index rendering 

    :param opcode: Specifies a symbolic constant that selects a logical operation. 
    :type opcode: typing.Union[int, str]
    '''

    pass


def glMap1(target: typing.Union[int, str], u1, u2, stride: int, order: int,
           points: 'Buffer'):
    '''Define a one-dimensional evaluator 

    :param target: Specifies the kind of values that are generated by the evaluator. 
    :type target: typing.Union[int, str]
    :param u2: Specify a linear mapping of u, as presented to glEvalCoord1, to ^, t he variable that is evaluated by the equations specified by this command. 
    :param stride: Specifies the number of floats or float (double)s between the beginning of one control point and the beginning of the next one in the data structure referenced in points. This allows control points to be embedded in arbitrary data structures. The only constraint is that the values for a particular control point must occupy contiguous memory locations. 
    :type stride: int
    :param order: Specifies the number of control points. Must be positive. 
    :type order: int
    :param points: Specifies a pointer to the array of control points. 
    :type points: 'Buffer'
    '''

    pass


def glMap2(target: typing.Union[int, str], u1, u2, ustride: int, uorder: int,
           v1, v2, vstride: int, vorder: int, points: 'Buffer'):
    '''Define a two-dimensional evaluator 

    :param target: Specifies the kind of values that are generated by the evaluator. 
    :type target: typing.Union[int, str]
    :param u2: Specify a linear mapping of u, as presented to glEvalCoord2, to ^, t he variable that is evaluated by the equations specified by this command. Initially u1 is 0 and u2 is 1. 
    :param ustride: Specifies the number of floats or float (double)s between the beginning of control point R and the beginning of control point R ij, where i and j are the u and v control point indices, respectively. This allows control points to be embedded in arbitrary data structures. The only constraint is that the values for a particular control point must occupy contiguous memory locations. The initial value of ustride is 0. 
    :type ustride: int
    :param uorder: Specifies the dimension of the control point array in the u axis. Must be positive. The initial value is 1. 
    :type uorder: int
    :param v2: Specify a linear mapping of v, as presented to glEvalCoord2, to ^, one of the two variables that are evaluated by the equations specified by this command. Initially, v1 is 0 and v2 is 1. 
    :param vstride: Specifies the number of floats or float (double)s between the beginning of control point R and the beginning of control point R ij, where i and j are the u and v control point(indices, respectively. This allows control points to be embedded in arbitrary data structures. The only constraint is that the values for a particular control point must occupy contiguous memory locations. The initial value of vstride is 0. 
    :type vstride: int
    :param vorder: Specifies the dimension of the control point array in the v axis. Must be positive. The initial value is 1. 
    :type vorder: int
    :param points: Specifies a pointer to the array of control points. 
    :type points: 'Buffer'
    '''

    pass


def glMapGrid(un: int, u1, u2, vn: int, v1, v2):
    '''Define a one- or two-dimensional mesh 

    :param un: Specifies the number of partitions in the grid range interval [u1, u2]. Must be positive. 
    :type un: int
    :param u2: Specify the mappings for integer grid domain values i=0 and i=un. 
    :param vn: Specifies the number of partitions in the grid range interval [v1, v2] (glMapGrid2 only). 
    :type vn: int
    :param v2: Specify the mappings for integer grid domain values j=0 and j=vn (glMapGrid2 only). 
    '''

    pass


def glMaterial(face: typing.Union[int, str], pname: typing.Union[int, str],
               params: int):
    '''Specify material parameters for the lighting model. 

    :param face: Specifies which face or faces are being updated. Must be one of: 
    :type face: typing.Union[int, str]
    :param pname: Specifies the single-valued material parameter of the face or faces that is being updated. Must be GL_SHININESS. 
    :type pname: typing.Union[int, str]
    :param params: Specifies the value that parameter GL_SHININESS will be set to. If function prototype ends in 'v' specifies a pointer to the value or values that pname will be set to. 
    :type params: int
    '''

    pass


def glMatrixMode(mode: typing.Union[int, str]):
    '''Specify which matrix is the current matrix. 

    :param mode: Specifies which matrix stack is the target for subsequent matrix operations. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glMultMatrix(m: 'Buffer'):
    '''Multiply the current matrix with the specified matrix 

    :param m: Points to 16 consecutive values that are used as the elements of a 4x4 column major matrix. 
    :type m: 'Buffer'
    '''

    pass


def glNewList(list: int, mode: typing.Union[int, str]):
    '''Create or replace a display list 

    :param list: Specifies the display list name 
    :type list: int
    :param mode: Specifies the compilation mode. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glNormal3(nx, ny, nz, v: 'Buffer'):
    '''Set the current normal vector 

    :param nz: Specify the x, y, and z coordinates of the new current normal. The initial value of the current normal is the unit vector, (0, 0, 1). 
    :param v: Specifies a pointer to an array of three elements: the x, y, and z coordinates of the new current normal. 
    :type v: 'Buffer'
    '''

    pass


def glOrtho(left, right, bottom, top, zNear, zFar):
    '''Multiply the current matrix with an orthographic matrix 

    :param right: Specify the coordinates for the left and right vertical clipping planes. 
    :param top: Specify the coordinates for the bottom and top horizontal clipping planes. 
    :param zFar: Specify the distances to the nearer and farther depth clipping planes. These values are negative if the plane is to be behind the viewer. 
    '''

    pass


def glPassThrough(token: float):
    '''Place a marker in the feedback buffer 

    :param token: Specifies a marker value to be placed in the feedback buffer following a GL_PASS_THROUGH_TOKEN. 
    :type token: float
    '''

    pass


def glPixelMap(map: typing.Union[int, str], mapsize: int, values: 'Buffer'):
    '''Set up pixel transfer maps 

    :param map: Specifies a symbolic map name. 
    :type map: typing.Union[int, str]
    :param mapsize: Specifies the size of the map being defined. 
    :type mapsize: int
    :param values: Specifies an array of mapsize values. 
    :type values: 'Buffer'
    '''

    pass


def glPixelStore(pname: typing.Union[int, str], param):
    '''Set pixel storage modes 

    :param pname: Specifies the symbolic name of the parameter to be set. Six values affect the packing of pixel data into memory. Six more affect the unpacking of pixel data from memory. 
    :type pname: typing.Union[int, str]
    :param param: Specifies the value that pname is set to. 
    '''

    pass


def glPixelTransfer(pname: typing.Union[int, str], param):
    '''Set pixel transfer modes 

    :param pname: Specifies the symbolic name of the pixel transfer parameter to be set. 
    :type pname: typing.Union[int, str]
    :param param: Specifies the value that pname is set to. 
    '''

    pass


def glPixelZoom(xfactor, yfactor):
    '''Specify the pixel zoom factors 

    :param yfactor: Specify the x and y zoom factors for pixel write operations. 
    '''

    pass


def glPointSize(size: float):
    '''Specify the diameter of rasterized points 

    :param size: Specifies the diameter of rasterized points. The initial value is 1. 
    :type size: float
    '''

    pass


def glPolygonMode(face: typing.Union[int, str], mode: typing.Union[int, str]):
    '''Select a polygon rasterization mode 

    :param face: Specifies the polygons that mode applies to. Must be GL_FRONT for front-facing polygons, GL_BACK for back- facing polygons, or GL_FRONT_AND_BACK for front- and back-facing polygons. 
    :type face: typing.Union[int, str]
    :param mode: Specifies how polygons will be rasterized. The initial value is GL_FILL for both front- and back- facing polygons. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glPolygonOffset(factor: float, units: float):
    '''Set the scale and units used to calculate depth values 

    :param factor: Specifies a scale factor that is used to create a variable depth offset for each polygon. The initial value is 0. 
    :type factor: float
    :param units: Is multiplied by an implementation-specific value to create a constant depth offset. The initial value is 0. 
    :type units: float
    '''

    pass


def glPolygonStipple(mask: 'bpy.context.object'):
    '''Set the polygon stippling pattern 

    :param mask: Specifies a pointer to a 32x32 stipple pattern that will be unpacked from memory in the same way that glDrawPixels unpacks pixels. 
    :type mask: 'bpy.context.object'
    '''

    pass


def glPopAttrib():
    '''Pop the server attribute stack 

    '''

    pass


def glPopClientAttrib():
    '''Pop the client attribute stack 

    '''

    pass


def glPopMatrix():
    '''Pop the current matrix stack 

    '''

    pass


def glPopName():
    '''Pop the name stack 

    '''

    pass


def glPrioritizeTextures(n: int, textures: 'Buffer', priorities: 'Buffer'):
    '''Set texture residence priority 

    :param n: Specifies the number of textures to be prioritized. 
    :type n: int
    :param textures: Specifies an array containing the names of the textures to be prioritized. 
    :type textures: 'Buffer'
    :param priorities: Specifies an array containing the texture priorities. A priority given in an element of priorities applies to the texture named by the corresponding element of textures. 
    :type priorities: 'Buffer'
    '''

    pass


def glPushAttrib(mask):
    '''Push the server attribute stack 

    :param mask: Specifies a mask that indicates which attributes to save. 
    '''

    pass


def glPushClientAttrib(mask):
    '''Push the client attribute stack 

    :param mask: Specifies a mask that indicates which attributes to save. 
    '''

    pass


def glPushMatrix():
    '''Push the current matrix stack 

    '''

    pass


def glPushName(name: int):
    '''Push the name stack 

    :param name: Specifies a name that will be pushed onto the name stack. 
    :type name: int
    '''

    pass


def glRasterPos(x, y, z, w):
    '''Specify the raster position for pixel operations 

    :param w: Specify the x,y,z, and w object coordinates (if present) for the raster position. If function prototype ends in 'v' specifies a pointer to an array of two, three, or four elements, specifying x, y, z, and w coordinates, respectively. 
    '''

    pass


def glReadBuffer(mode: typing.Union[int, str]):
    '''Select a color buffer source for pixels. 

    :param mode: Specifies a color buffer. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glReadPixels(x, y, width, height, format: typing.Union[int, str],
                 type: typing.Union[int, str], pixels: 'bpy.context.object'):
    '''Read a block of pixels from the frame buffer 

    :param y: Specify the window coordinates of the first pixel that is read from the frame buffer. This location is the lower left corner of a rectangular block of pixels. 
    :param height: Specify the dimensions of the pixel rectangle. width and height of one correspond to a single pixel. 
    :param format: Specifies the format of the pixel data. 
    :type format: typing.Union[int, str]
    :param type: Specifies the data type of the pixel data. 
    :type type: typing.Union[int, str]
    :param pixels: Returns the pixel data. 
    :type pixels: 'bpy.context.object'
    '''

    pass


def glRect(x1, y1, x2, y2, v1, v2):
    '''Draw a rectangle 

    :param y1: Specify one vertex of a rectangle 
    :param y2: Specify the opposite vertex of the rectangle 
    :param v2: Specifies a pointer to one vertex of a rectangle and the pointer to the opposite vertex of the rectangle 
    '''

    pass


def glRenderMode(mode: typing.Union[int, str]):
    '''Set rasterization mode 

    :param mode: Specifies the rasterization mode. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glRotate(angle, x, y, z):
    '''Multiply the current matrix by a rotation matrix 

    :param angle: Specifies the angle of rotation in degrees. 
    :param z: Specify the x, y, and z coordinates of a vector respectively. 
    '''

    pass


def glScale(x, y, z):
    '''Multiply the current matrix by a general scaling matrix 

    :param z: Specify scale factors along the x, y, and z axes, respectively. 
    '''

    pass


def glScissor(x, y, width, height):
    '''Define the scissor box 

    :param y: Specify the lower left corner of the scissor box. Initially (0, 0). 
    :param height: Specify the width and height of the scissor box. When a GL context is first attached to a window, width and height are set to the dimensions of that window. 
    '''

    pass


def glSelectBuffer(size: int, buffer: 'Buffer'):
    '''Establish a buffer for selection mode values 

    :param size: Specifies the size of buffer 
    :type size: int
    :param buffer: Returns the selection data 
    :type buffer: 'Buffer'
    '''

    pass


def glShadeModel(mode: typing.Union[int, str]):
    '''Select flat or smooth shading 

    :param mode: Specifies a symbolic value representing a shading technique. 
    :type mode: typing.Union[int, str]
    '''

    pass


def glShaderSource(shader: int, shader_string: str):
    '''Replaces the source code in a shader object. 

    :param shader: Specifies the handle of the shader object whose source code is to be replaced. 
    :type shader: int
    :param shader_string: The shader string. 
    :type shader_string: str
    '''

    pass


def glStencilFunc(func: typing.Union[int, str], ref: int, mask: int):
    '''Set function and reference value for stencil testing 

    :param func: Specifies the test function. 
    :type func: typing.Union[int, str]
    :param ref: Specifies the reference value for the stencil test. ref is clamped to the range [0,2n-1], where n is the number of bitplanes in the stencil buffer. The initial value is 0. 
    :type ref: int
    :param mask: Specifies a mask that is ANDed with both the reference value and the stored stencil value when the test is done. The initial value is all 1's. 
    :type mask: int
    '''

    pass


def glStencilMask(mask: int):
    '''Control the writing of individual bits in the stencil planes 

    :param mask: Specifies a bit mask to enable and disable writing of individual bits in the stencil planes. Initially, the mask is all 1's. 
    :type mask: int
    '''

    pass


def glStencilOp(fail: typing.Union[int, str], zfail: typing.Union[int, str],
                zpass: typing.Union[int, str]):
    '''Set stencil test actions 

    :param fail: Specifies the action to take when the stencil test fails. The initial value is GL_KEEP. 
    :type fail: typing.Union[int, str]
    :param zfail: Specifies the stencil action when the stencil test passes, but the depth test fails. zfail accepts the same symbolic constants as fail. The initial value is GL_KEEP. 
    :type zfail: typing.Union[int, str]
    :param zpass: Specifies the stencil action when both the stencil test and the depth test pass, or when the stencil test passes and either there is no depth buffer or depth testing is not enabled. zpass accepts the same symbolic constants as fail. The initial value is GL_KEEP. 
    :type zpass: typing.Union[int, str]
    '''

    pass


def glTexCoord(s, t, r, q, v: 'Buffer'):
    '''Set the current texture coordinates 

    :param q: Specify s, t, r, and q texture coordinates. Not all parameters are present in all forms of the command. 
    :param v: Specifies a pointer to an array of one, two, three, or four elements, which in turn specify the s, t, r, and q texture coordinates. 
    :type v: 'Buffer'
    '''

    pass


def glTexEnv(target: typing.Union[int, str], pname: typing.Union[int, str],
             param):
    '''Set texture environment parameters 

    :param target: Specifies a texture environment. Must be GL_TEXTURE_ENV. 
    :type target: typing.Union[int, str]
    :param pname: Specifies the symbolic name of a single-valued texture environment parameter. Must be GL_TEXTURE_ENV_MODE. 
    :type pname: typing.Union[int, str]
    :param param: Specifies a single symbolic constant. If function prototype ends in 'v' specifies a pointer to a parameter array that contains either a single symbolic constant or an RGBA color 
    '''

    pass


def glTexGen(coord: typing.Union[int, str], pname: typing.Union[int, str],
             param):
    '''Control the generation of texture coordinates 

    :param coord: Specifies a texture coordinate. 
    :type coord: typing.Union[int, str]
    :param pname: Specifies the symbolic name of the texture- coordinate generation function. 
    :type pname: typing.Union[int, str]
    :param param: Specifies a single-valued texture generation parameter. If function prototype ends in 'v' specifies a pointer to an array of texture generation parameters. If pname is GL_TEXTURE_GEN_MODE, then the array must contain a single symbolic constant. Otherwise, params holds the coefficients for the texture-coordinate generation function specified by pname. 
    '''

    pass


def glTexImage1D(target: typing.Union[int, str], level: int,
                 internalformat: int, width: int, border: int,
                 format: typing.Union[int, str], type: typing.Union[int, str],
                 pixels: 'Buffer'):
    '''Specify a one-dimensional texture image 

    :param target: Specifies the target texture. 
    :type target: typing.Union[int, str]
    :param level: Specifies the level-of-detail number. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param internalformat: Specifies the number of color components in the texture. 
    :type internalformat: int
    :param width: Specifies the width of the texture image. Must be 2n+2(border) for some integer n. All implementations support texture images that are at least 64 texels wide. The height of the 1D texture image is 1. 
    :type width: int
    :param border: Specifies the width of the border. Must be either 0 or 1. 
    :type border: int
    :param format: Specifies the format of the pixel data. 
    :type format: typing.Union[int, str]
    :param type: Specifies the data type of the pixel data. 
    :type type: typing.Union[int, str]
    :param pixels: Specifies a pointer to the image data in memory. 
    :type pixels: 'Buffer'
    '''

    pass


def glTexImage2D(target: typing.Union[int, str], level: int,
                 internalformat: int, width: int, height: int, border: int,
                 format: typing.Union[int, str], type: typing.Union[int, str],
                 pixels: 'Buffer'):
    '''Specify a two-dimensional texture image 

    :param target: Specifies the target texture. 
    :type target: typing.Union[int, str]
    :param level: Specifies the level-of-detail number. Level 0 is the base image level. Level n is the nth mipmap reduction image. 
    :type level: int
    :param internalformat: Specifies the number of color components in the texture. 
    :type internalformat: int
    :param width: Specifies the width of the texture image. Must be 2n+2(border) for some integer n. All implementations support texture images that are at least 64 texels wide. 
    :type width: int
    :param height: Specifies the height of the texture image. Must be 2m+2(border) for some integer m. All implementations support texture images that are at least 64 texels high. 
    :type height: int
    :param border: Specifies the width of the border. Must be either 0 or 1. 
    :type border: int
    :param format: Specifies the format of the pixel data. 
    :type format: typing.Union[int, str]
    :param type: Specifies the data type of the pixel data. 
    :type type: typing.Union[int, str]
    :param pixels: Specifies a pointer to the image data in memory. 
    :type pixels: 'Buffer'
    '''

    pass


def glTexParameter(target: typing.Union[int, str],
                   pname: typing.Union[int, str], param):
    '''Set texture parameters 

    :param target: Specifies the target texture. 
    :type target: typing.Union[int, str]
    :param pname: Specifies the symbolic name of a single-valued texture parameter. 
    :type pname: typing.Union[int, str]
    :param param: Specifies the value of pname. If function prototype ends in 'v' specifies a pointer to an array where the value or values of pname are stored. 
    '''

    pass


def glTranslate(x, y, z):
    '''Multiply the current matrix by a translation matrix 

    :param z: Specify the x, y, and z coordinates of a translation vector. 
    '''

    pass


def glUseProgram(program: int):
    '''Installs a program object as part of current rendering state 

    :param program: Specifies the handle of the program object whose executables are to be used as part of current rendering state. 
    :type program: int
    '''

    pass


def glValidateProgram(program: int):
    '''Validates a program object 

    :param program: Specifies the handle of the program object to be validated. 
    :type program: int
    '''

    pass


def glVertex(x, y, z, w, v: 'Buffer'):
    '''Specify a vertex 

    :param w: Specify x, y, z, and w coordinates of a vertex. Not all parameters are present in all forms of the command. 
    :param v: Specifies a pointer to an array of two, three, or four elements. The elements of a two-element array are x and y; of a three-element array, x, y, and z; and of a four-element array, x, y, z, and w. 
    :type v: 'Buffer'
    '''

    pass


def glViewport(x, y, width, height):
    '''Set the viewport 

    :param y: Specify the lower left corner of the viewport rectangle, in pixels. The initial value is (0,0). 
    :param height: Specify the width and height of the viewport. When a GL context is first attached to a window, width and height are set to the dimensions of that window. 
    '''

    pass


def gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz):
    '''Define a viewing transformation. 

    :param eyez: Specifies the position of the eye point. 
    :param centerz: Specifies the position of the reference point. 
    :param upz: Specifies the direction of the up vector. 
    '''

    pass


def gluOrtho2D(left, right, bottom, top):
    '''Define a 2-D orthographic projection matrix. 

    :param right: Specify the coordinates for the left and right vertical clipping planes. 
    :param top: Specify the coordinates for the bottom and top horizontal clipping planes. 
    '''

    pass


def gluPerspective(fovY, aspect, zNear, zFar):
    '''Set up a perspective projection matrix. 

    :param fovY: Specifies the field of view angle, in degrees, in the y direction. 
    :param aspect: Specifies the aspect ratio that determines the field of view in the x direction. The aspect ratio is the ratio of x (width) to y (height). 
    :param zNear: Specifies the distance from the viewer to the near clipping plane (always positive). 
    :param zFar: Specifies the distance from the viewer to the far clipping plane (always positive). 
    '''

    pass


def gluPickMatrix(x, y, width, height, viewport: 'Buffer'):
    '''Define a picking region. 

    :param y: Specify the center of a picking region in window coordinates. 
    :param height: Specify the width and height, respectively, of the picking region in window coordinates. 
    :param viewport: Specifies the current viewport. 
    :type viewport: 'Buffer'
    '''

    pass


def gluProject(objx, objy, objz, modelMatrix: 'Buffer', projMatrix: 'Buffer',
               viewport: 'Buffer', winx, winy, winz):
    '''Map object coordinates to window coordinates. 

    :param objz: Specify the object coordinates. 
    :param modelMatrix: Specifies the current modelview matrix (as from a glGetDoublev call). 
    :type modelMatrix: 'Buffer'
    :param projMatrix: Specifies the current projection matrix (as from a glGetDoublev call). 
    :type projMatrix: 'Buffer'
    :param viewport: Specifies the current viewport (as from a glGetIntegerv call). 
    :type viewport: 'Buffer'
    :param winz: Return the computed window coordinates. 
    '''

    pass


def gluUnProject(winx, winy, winz, modelMatrix: 'Buffer', projMatrix: 'Buffer',
                 viewport: 'Buffer', objx, objy, objz):
    '''Map object coordinates to window coordinates. 

    :param winz: Specify the window coordinates to be mapped. 
    :param modelMatrix: Specifies the current modelview matrix (as from a glGetDoublev call). 
    :type modelMatrix: 'Buffer'
    :param projMatrix: Specifies the current projection matrix (as from a glGetDoublev call). 
    :type projMatrix: 'Buffer'
    :param viewport: Specifies the current viewport (as from a glGetIntegerv call). 
    :type viewport: 'Buffer'
    :param objz: Return the computed object coordinates. 
    '''

    pass
