function circle (circleColor: number, milliseconds: number) {
    for (let led3 = 0; led3 <= 59; led3++) {
        haloDisplay.setZipLedColor(led3, circleColor)
        haloDisplay.show()
        basic.pause(milliseconds)
        haloDisplay.setZipLedColor(led3, kitronik_halo_hd.colors(ZipLedColors.Black))
    }
}
let haloDisplay: kitronik_halo_hd.ZIPHaloHd = null
let colors: number[] = []
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
let led2 = 0
haloDisplay.setBrightness(111)
haloDisplay.clear()
while (true) {
    for (let color of colors) {
        circle(color, 1000)
    }
}
