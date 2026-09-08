vim.opt.compatible = false
vim.cmd('filetype plugin indent on')
vim.cmd('syntax on')

vim.opt.number = true
vim.opt.relativenumber = true
vim.opt.shiftwidth = 4
vim.opt.tabstop = 4
vim.opt.encoding = "utf-8"
vim.opt.completeopt = { "menuone", "noinsert", "noselect" }
vim.opt.laststatus = 2
vim.opt.clipboard = "unnamedplus"
vim.opt.mouse = "a"
vim.opt.splitright = true
vim.opt.splitbelow = true
vim.opt.wildmenu = true
vim.opt.autoindent = true
vim.opt.smartindent = true
vim.opt.showcmd = true
vim.opt.showmode = false
vim.opt.cursorline = false
vim.opt.colorcolumn = "85"
vim.cmd [[
	autocmd FileType netrw setlocal colorcolumn=0
]]
vim.opt.signcolumn = "yes"

vim.cmd('colorscheme retrobox')

-- Shell Detection
if vim.fn.executable('zsh') == 1 then
    vim.opt.shell = 'zsh'
else
    vim.opt.shell = 'bash'
end

-- Search
vim.opt.incsearch = true
vim.opt.ignorecase = true
vim.opt.smartcase = true
vim.opt.showmatch = true
vim.opt.hlsearch = true

-- Netrw
vim.g.netrw_liststyle = 0

-- Indentation line colour
vim.cmd.highlight('IndentLine guifg=#292E42')
vim.cmd.highlight('IndentLineCurrent guifg=#FFFFFF')
