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
