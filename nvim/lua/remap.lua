local map = vim.keymap.set

map('n', '<space>', ':nohlsearch<CR>', { silent = true })

-- Window Navigation
map('n', '<C-j>', '<C-w>j')
map('n', '<C-k>', '<C-w>k')
map('n', '<C-h>', '<C-w>h')
map('n', '<C-l>', '<C-w>l')

-- Window Resizing
map('n', '<C-Up>', '<C-w>+')
map('n', '<C-Down>', '<C-w>-')
map('n', '<C-Left>', '<C-w><')
map('n', '<C-Right>', '<C-w>>')

-- Tabs & Explorer
map('n', '<leader><tab>', ':tabnext<CR>')
map('n', '<leader><S-tab>', ':tabprevious<CR>')
map('n', '<leader>b', ':Rexplore<CR>')

-- Terminal Mode
map('t', '<C-w>', [[<C-\><C-n>]])
