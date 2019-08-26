" Enable syntax-highlighting
syntax on

" Use line numbering
set number

" Use custom colorscheme
colorscheme desert

" Remap window navigation 
" for use in MS Windows to avoid Ctrl-w
nnoremap gh <C-w><C-h>
nnoremap gl <C-w><C-l>
nnoremap gj <C-w><C-j>
nnoremap gk <C-w><C-k>

" File-type specific settings
if has("autocmd")

  filetype plugin on

  "Python code : use 4 spaces, no tabs
  augroup python
    autocmd BufReadPre,FileReadPre    *.py set tabstop=4
    autocmd BufReadPre,FileReadPre    *.py set expandtab
  augroup END
endif
