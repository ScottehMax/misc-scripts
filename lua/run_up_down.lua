-- runs = 0
-- curexp = 3417
-- wantedexp = 186096
-- neededexp = wantedexp - curexp
-- steps = 86
-- totalruns = math.ceil(neededexp/steps)

totalruns = 10000
runs = 0

runlen = 210


print(string.format("doing %d runs", totalruns))

use_b = false

while runs < totalruns do
    print(runs)
    i = 0
    while i < runlen do
        joypad.set(1, {up=true, B=use_b})
        emu.frameadvance()
        i = i + 1
    end

    i = 0
    while i < runlen do
        joypad.set(1, {down=true, B=use_b})
        emu.frameadvance()
        i = i + 1
    end

    -- joypad.set(1, {B=false})

    runs = runs + 1
end