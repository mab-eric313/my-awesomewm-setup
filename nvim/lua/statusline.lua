vim.api.nvim_set_hl(0, "VertSplit", {
	fg = "#aaaaaa",
	bg = "NONE",
	ctermfg = 0,
	ctermbg = 15
})
vim.api.nvim_set_hl(0, "SignColumn", {
	bg = "NONE",
	ctermbg = "NONE"
})
vim.api.nvim_set_hl(0, "LspReference", {
	fg = "#000000",
	bg = "#444444",
	ctermfg = 15,
	ctermbg = 8
})
vim.api.nvim_set_hl(0, "Search", {
	bg = "Yellow",
	fg = "Black",
	ctermfg = 0,
	ctermbg = 11
})
vim.api.nvim_set_hl(0, "ModeMsg", {
	bg = "Black",
	fg = "White",
	ctermfg = 14,
	ctermbg = 15
})
vim.api.nvim_set_hl(0, "PmenuSel", {
	bg = "Black",
	fg = "White",
	ctermfg = 14,
	ctermbg = 15
})

-- Statusline Implementation
local modes = {
    ['n']      = 'NORMAL',
    ['i']      = 'INSERT',
    ['v']      = 'VISUAL',
    ['V']      = 'VISUAL-LINE',
    ['\22']    = 'VISUAL-BLOCK', -- <C-V>
    ['R']      = 'REPLACE',
    ['c']      = 'COMMAND',
    ['nt']     = 'NTERMINAL',
    ['t']      = 'TERMINAL',
}

_G.update_statusline = function()
    local m = vim.api.nvim_get_mode().mode
    local current_mode = modes[m] or m
    return string.format(" %%#ModeMsg# %s %%#StatusLine# %%t %%m %%r %%y %%= %%#PmenuSel# col:%%c cur:%%l last:%%L %%p%%%% ", current_mode)
end

vim.opt.statusline = "%!v:lua.update_statusline()"
