local function augroup(name)
    return vim.api.nvim_create_augroup(name, { clear = true })
end

-- Netrw Sync CWD
local function netrw_sync_cwd()
    local curdir = vim.b.netrw_curdir
    if curdir then
        vim.cmd('lcd ' .. vim.fn.fnameescape(curdir))
    end
end

vim.api.nvim_create_autocmd("FileType", {
    group = augroup("netrw_to_cwd"),
    pattern = { "netrw" },
    callback = netrw_sync_cwd,
})

vim.api.nvim_create_autocmd("FileType", {
    pattern = { "yaml" },
    callback = function ()
      vim.opt.tabstop = 2
      vim.opt.shiftwidth = 2
      vim.opt.expandtab = false
    end,
})

vim.api.nvim_create_autocmd("FileType", {
    -- pattern = { },
    callback = function ()
      vim.opt.tabstop = 4
      vim.opt.shiftwidth = 4
      vim.opt.expandtab = false
    end,
})

vim.api.nvim_create_autocmd("FileType", {
    pattern = { "python" },
    callback = function ()
		vim.opt.tabstop = 4
		vim.opt.shiftwidth = 4
		vim.opt.expandtab = false
		vim.opt.colorcolumn = "80"
    end,
})

vim.api.nvim_create_autocmd("FileType", {
    pattern = { "svelte", "blade" },
    callback = function ()
    	vim.opt.filetype = "html"
    end,
})

vim.api.nvim_create_autocmd("FileType", {
    pattern = { "dart", "flutter", "json" },
    callback = function ()
    	vim.opt.tabstop = 2
    	vim.opt.shiftwidth = 2
    	vim.opt.expandtab = true
    end,
})

-- Netrw Settings
vim.g.netrw_bufsettings = 'noma nomod relativenumber nobl nowrap ro'
