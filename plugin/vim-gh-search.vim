let s:root_dir = fnamemodify(resolve(expand('<sfile>:p')), ':h')

python3 << EOF
import sys
import subprocess
from os.path import normpath, join
import vim
root_dir = vim.eval('s:root_dir')
python_root_dir = normpath(join(root_dir, '..', 'python'))
sys.path.insert(0, python_root_dir)
from vim_gh_search import *
EOF

function! s:search()
python3 << EOF
main(vim.eval('s:params'))
EOF
endfunction

function! GhSearch()
let s:params = input('Search: ')
call s:search()
endfunction

function GhSearchSelected()
let s:params = @*
call s:search()
endfunction

vnoremap gs :call GhSearchSelected()<CR> 

command! -nargs=0 GhSearch call GhSearch()
command! -nargs=0 GhSearchSelected call GhSearchSelected()
