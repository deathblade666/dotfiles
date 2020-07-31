set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" Install L9 and avoid a Naming conflict if you've already installed a
" different version somewhere else.
" Plugin 'ascenator/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required

" To ignore plugin indent changes, instead use:
"filetype plugin on

" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just
" :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to
" auto-approve removal

" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" => Powerline
" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
packadd! dracula
syntax enable
colorscheme dracula 

" Use 256 colours (Use this setting only if your terminal supports 256
" colours)
set t_Co=256

" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" " =>  Enable numbered rows
" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set number
"
" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" " => Mouse Scrolling
" """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set mouse=nicr
