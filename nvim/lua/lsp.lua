require("mason").setup()
require("mason-lspconfig").setup()

local capabilities = require("cmp_nvim_lsp").default_capabilities()
capabilities.textDocument.completion.completionItem.snippetSupport = true

vim.lsp.config()

vim.lsp.enable({})

vim.g.lsp_log_verbose = 1
vim.g.lsp_diagnostics_enabled = 1
vim.g.lsp_diagnostics_delay = 100
vim.g.lsp_diagnostics_virtual_text_enabled = 0
vim.g.lsp_diagnostics_signs_enabled = 1
vim.g.lsp_diagnostics_echo_cursor = 1
vim.g.lsp_document_highlight_enabled = 1
vim.g.lsp_code_lens_enabled = 0
vim.g.lsp_signature_help_enabled = 0

vim.diagnostic.config({
	virtual_text = true,
})

vim.api.nvim_create_autocmd("LspAttach", {
	desc = "LSP actions",
	callback = function(event)
		local opts = { buffer = event.buf }
		local client = assert(vim.lsp.get_client_by_id(event.data.client_id))

		if not client then
			return
		end

		if client:supports_method("textDocument/implementation") then
			vim.keymap.set("n", "K", "<cmd>lua vim.lsp.buf.hover()<cr>", opts)
			vim.keymap.set("n", "gd", "<cmd>lua vim.lsp.buf.definition()<cr>", opts)
			vim.keymap.set("n", "gD", "<cmd>lua vim.lsp.buf.declaration()<cr>", opts)
			vim.keymap.set("n", "gi", "<cmd>lua vim.lsp.buf.implementation()<cr>", opts)
			vim.keymap.set("n", "go", "<cmd>lua vim.lsp.buf.type_definition()<cr>", opts)
			vim.keymap.set("n", "gr", "<cmd>lua vim.lsp.buf.references()<cr>", opts)
			vim.keymap.set("n", "gs", "<cmd>lua vim.lsp.buf.signature_help()<cr>", opts)
			vim.keymap.set("n", "<F2>", "<cmd>lua vim.lsp.buf.rename()<cr>", opts)
			vim.keymap.set({ "n", "x" }, "<F3>", "<cmd>lua vim.lsp.buf.format({async = true})<cr>", opts)
			vim.keymap.set("n", "<F4>", "<cmd>lua vim.lsp.buf.code_action()<cr>", opts)
		end
	end,
})

local cmp = require("cmp")
cmp.setup({
	sources = {
		{ name = "nvim_lsp" },
	},
	snippet = {
		expand = function(args)
			vim.snippet.expand(args.body)
		end,
	},
	mapping = cmp.mapping.preset.insert({}),
})
