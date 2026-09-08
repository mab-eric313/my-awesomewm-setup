return require("packer").startup(function(use)
	use("wbthomason/packer.nvim")

	-- LSP
	use({
		"neovim/nvim-lspconfig",
		requires = {
			"williamboman/mason.nvim",
			"williamboman/mason-lspconfig.nvim",
		},
	})
	use("hrsh7th/nvim-cmp")
	use("hrsh7th/cmp-nvim-lsp")
	use({
		"esmuellert/nvim-eslint",
		config = function()
			require("nvim-eslint").setup({})
		end,
	})

	-- Indent
	use({
		"nvimdev/indentmini.nvim",
		config = function()
			require("indentmini").setup({
				minlevel = 2,
				exclude = { "markdown", "help", "text", "rst" },
				exclude_nodetype = { "string", "comment" },
			})
		end,
	})

	-- Syntax
	use({
		"nvim-treesitter/nvim-treesitter",
		run = ":TSUpdate",
		config = function()
		  require("nvim-treesitter.config").setup({
			ensure_installed = { "c", "lua", "vim", "c3" },
			highlight = {
			  enable = true,
			},
		  })
		end,
	})
end)
