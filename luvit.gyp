{
  'targets': [
    {'target_name': 'libluvit',
     'type': 'static_library',
     'dependencies': [
       'deps/http-parser/http_parser.gyp:http_parser',
       'deps/luajit.gyp:*',
       'deps/yajl.gyp:yajl',
       'deps/uv/uv.gyp:uv',
     ],
     'export_dependent_settings': [
       'deps/http-parser/http_parser.gyp:http_parser',
       'deps/luajit.gyp:*',
       'deps/yajl.gyp:yajl',
       'deps/uv/uv.gyp:uv',
      ],
      'conditions': [
        ['OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"', {
          'cflags': [ '--std=c89' ],
          'defines': [ '_GNU_SOURCE' ]
        }],
      ],
     'sources': [
       'src/lconstants.c',
       'src/lenv.c',
       'src/lhttp_parser.c',
       'src/lyajl.c',
       'src/los.c',
       'src/luv.c',
       'src/luv_fs.c',
       'src/luv_fs_watcher.c',
       'src/luv_dns.c',
       'src/luv_handle.c',
       'src/luv_misc.c',
       'src/luv_pipe.c',
       'src/luv_process.c',
       'src/luv_stream.c',
       'src/luv_tcp.c',
       'src/luv_timer.c',
       'src/luv_tty.c',
       'src/luv_udp.c',
       'src/luvit_init.c',
       'src/lyajl.c',
       'src/utils.c',
       'lib/luvit/buffer.lua',
       'lib/luvit/childprocess.lua',
       'lib/luvit/core.lua',
       'lib/luvit/dns.lua',
       'lib/luvit/fiber.lua',
       'lib/luvit/fs.lua',
       'lib/luvit/http.lua',
       'lib/luvit/json.lua',
       'lib/luvit/luvit.lua',
       'lib/luvit/mime.lua',
       'lib/luvit/net.lua',
       'lib/luvit/path.lua',
       'lib/luvit/pipe.lua',
       'lib/luvit/querystring.lua',
       'lib/luvit/repl.lua',
       'lib/luvit/stack.lua',
       'lib/luvit/tcp.lua',
       'lib/luvit/timer.lua',
       'lib/luvit/tty.lua',
       'lib/luvit/udp.lua',
       'lib/luvit/url.lua',
       'lib/luvit/utils.lua',
     ],
     'defines': [
       'LUVIT_OS="<(OS)"',
       'LUVIT_VERSION="<!(git --git-dir .git describe --tags)"',
       'HTTP_VERSION="<!(git --git-dir deps/http-parser/.git describe --tags)"',
       'UV_VERSION="<!(git --git-dir deps/uv/.git describe --all --tags --always --long)"',
       'LUAJIT_VERSION="<!(git --git-dir deps/luajit/.git describe --tags)"',
       'YAJL_VERSIONISH="<!(git --git-dir deps/yajl/.git describe --tags)"',
       'BUNDLE=1',
     ],
     'include_dirs': [
       'src',
       'deps/uv/src/ares'
     ],
     'direct_dependent_settings': {
       'include_dirs': [
         'src',
         'deps/uv/src/ares'
       ]
     },
     'rules': [
       {
         'rule_name': 'jit_lua',
         'extension': 'lua',
         'outputs': [
           '<(SHARED_INTERMEDIATE_DIR)/generated/<(RULE_INPUT_ROOT)_jit.c'
         ],
         'action': [
           '<(PRODUCT_DIR)/luajit',
           '-b', '<(RULE_INPUT_PATH)',
           '<(SHARED_INTERMEDIATE_DIR)/generated/<(RULE_INPUT_ROOT)_jit.c',
         ],
         'process_outputs_as_sources': 1,
         'message': 'luajit <(RULE_INPUT_PATH)'
       }
     ],
    },
    {
      'target_name': 'luvit',
      'type': 'executable',
      'dependencies': [
        'libluvit',
      ],
      'sources': [
        'src/luvit_main.c',
        'src/luvit_exports.c',
      ],
      'msvs-settings': {
        'VCLinkerTool': {
          'SubSystem': 1, # /subsystem:console
        },
      },
      'conditions': [
        ['OS == "linux"', {
          'libraries': ['-ldl'],
        }],
        ['OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"', {
          'cflags': [ '--std=c89' ],
          'defines': [ '_GNU_SOURCE' ]
        }],
      ],
      'defines': [ 'BUNDLE=1']
    },
    {
      'target_name': 'vector_luvit',
      'product_name': 'vector',
      'product_extension': 'luvit',
      'product_prefix': '',
      'type': 'shared_library',
      'dependencies': [
        'libluvit',
      ],
      'sources': [
        'examples/native/vector.c'
      ],
      'conditions': [
        ['OS=="linux" or OS=="freebsd" or OS=="openbsd" or OS=="solaris"', {
          'cflags': [ '--std=c89' ],
          'defines': [ '_GNU_SOURCE' ]
        }],
      ],
    }
  ],
}
