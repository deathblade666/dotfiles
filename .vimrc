"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Vundle For Managing Plugins
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim

call vundle#begin()	      " required, all plugins must appear after this line.

Plugin 'gmarik/Vundle.vim'    " Vundle
Plugin 'dracula/vim'
Plugin 'vifm/vifm.vim'
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Powerline
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
packadd! dracula
syntax enable
colorscheme dracula 

" Use 256 colours (Use this setting only if your terminal supports 256 colours)
set t_Co=256

:highlight Normal ctermbg=032541

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" =>  Enable numbered rows
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set number

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Mouse Scrolling
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set mouse=a


set autoindent
set incsearch
set shiftwidth=4
set softtabstop=4 
set smarttab
set smartindent

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"=> nnn.vim auto-open/close
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Start NnnExplorer and leave the cursor in it.
" autocmd VimEnter * call nnn#explorer()

" Start NnnExplorer and put the cursor back in the other window.
" autocmd VimEnter * call nnn#explorer() | wincmd p | stopinsert

" If a file is specified, start NnnExplorer and move the cursor to the file window.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() > 0 || exists("s:std_in") | call nnn#explorer() | wincmd p | stopinsert | endif

" Exit Vim if NnnExplorer is the only window remaining in the only tab.
" autocmd BufEnter * if tabpagenr('$') == 1 && winnr('$') == 1 && &filetype ==# 'nnn' | quit! | endif

" Close the tab if NnnExplorer is the only window remaining in it.
autocmd BufEnter * if winnr('$') == 1 && &filetype ==# 'nnn' | quit! | endif

