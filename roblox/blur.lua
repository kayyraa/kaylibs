local effect = {}

function effect.Blur(transparency: number, gui_element)
	-- Effect Esseintals
	local prefix = "rbxassetid://"
	local effect_id = "16150097838"
	
	-- Auto Color
	local r, g, b = gui_element.BackgroundColor3.R, gui_element.BackgroundColor3.G, gui_element.BackgroundColor3.B
	
	-- Blur Identify
	local blur = Instance.new("ImageLabel")
	blur.Image = prefix .. effect_id
	blur.ImageColor3 = Color3.fromRGB(r, g, b)
	blur.ImageTransparency = transparency
	blur.Parent = gui_element
	blur.LayoutOrder = 1
end

return effect
