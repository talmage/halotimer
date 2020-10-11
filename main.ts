function circle(circleColor: number, milliseconds: number) {
    for (let led3 = 0; led3 < 60; led3++) {
        haloDisplay.setZipLedColor(led3, circleColor)
        haloDisplay.show()
        basic.pause(milliseconds)
        haloDisplay.setZipLedColor(led3, kitronik_halo_hd.colors(ZipLedColors.Black))
    }
}

//  Press button A to decrease the brightness of the LED
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (brightness > 0) {
        brightness += -1
        haloDisplay.setBrightness(brightness)
    }
    
})
//  Press button B to increase the brightness of the LED
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showString("Brightness:")
    basic.showNumber(brightness)
})
//  Press button B to increase the brightness of the LED
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (brightness < 255) {
        brightness += 1
        haloDisplay.setBrightness(brightness)
    }
    
})
let haloDisplay : kitronik_halo_hd.ZIPHaloHd = null
let colors : number[] = []
let brightness = 0
let led2 = 0
brightness = 128
colors.push(kitronik_halo_hd.colors(ZipLedColors.Red))
colors.push(kitronik_halo_hd.colors(ZipLedColors.Orange))
colors.push(kitronik_halo_hd.colors(ZipLedColors.Yellow))
colors.push(kitronik_halo_hd.colors(ZipLedColors.Green))
colors.push(kitronik_halo_hd.colors(ZipLedColors.Blue))
colors.push(kitronik_halo_hd.colors(ZipLedColors.Indigo))
colors.push(kitronik_halo_hd.colors(ZipLedColors.Violet))
colors.push(kitronik_halo_hd.colors(ZipLedColors.Purple))
colors.push(kitronik_halo_hd.colors(ZipLedColors.White))
haloDisplay = kitronik_halo_hd.createZIPHaloDisplay(60)
haloDisplay.setBrightness(brightness)
haloDisplay.clear()
while (true) {
    for (let color of colors) {
        circle(color, 1000)
    }
}
