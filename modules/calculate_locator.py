class CalculateLocator:
    def __init__(self):
        pass
    
    def lida_locator(self, var_dat):
        var_temp = {}
        
        vd_key = 1  # mulai dari var_dat key 1
        vd_index = 1  # mulai dari index 1 untuk key pertama
        
        for i in range(1, 19):
            if i == 1:
                var_temp[i] = [-1000, var_dat[vd_key][vd_index] - 1900]
                vd_index = 2  # next ambil index 2
            elif i == 18:
                var_temp[i] = [var_temp[i - 1][1] + 1, var_dat[6][2] + 4000]
            else:
                var_temp[i] = [var_temp[i - 1][1] + 1, var_dat[vd_key][vd_index] - 1900]
                
                # geser index
                vd_index += 1
                if vd_index > 2:  # kalau sudah lewat index 2, ganti key var_dat berikutnya
                    vd_index = 0
                    vd_key += 1
                    if vd_key > 6:
                        vd_key = 1
        
        result_list = []
        for key in sorted(var_temp.keys()):
            result_list.extend(var_temp[key])
            
        result = " ".join(str(x) for x in result_list)
        
        return result
    
    def kclka_locator(self, var_data):
        var_dat = self.convert_locator(var_data)
        var_temp = {}
        
        vd_key = 1  # mulai dari var_dat key 1
        vd_index = 0  # mulai dari index 1 untuk key pertama
        
        for i in range(1, 19):
            if i == 1:
                var_temp[i] = [-1000, var_dat[vd_key][vd_index] + 1900]
                vd_index = 1  # next ambil index 1
            elif i == 18:
                var_temp[i] = [var_temp[i - 1][1] + 1, var_dat[6][2] + 1900]
            else:
                var_temp[i] = [var_temp[i - 1][1] + 1, var_dat[vd_key][vd_index] + 1900]
                
                # geser index
                vd_index += 1
                if vd_index > 2:  # kalau sudah lewat index 2, ganti key var_dat berikutnya
                    vd_index = 0
                    vd_key += 1
                    if vd_key > 6:
                        vd_key = 1
        
        result_list = []
        for key in sorted(var_temp.keys()):
            result_list.extend(var_temp[key])
            
        result = " ".join(str(x) for x in result_list)
        return result
        
    def convert_locator(self, var_dat):
        upper_limit = 3751
        lower_limit = 3813
        var_temp = {}
        for i in range(1, 7):
            var_temp[i] = [
                var_dat[i] - upper_limit,
                var_dat[i],
                var_dat[i] + lower_limit
            ]
        return var_temp

def main():
    calc = CalculateLocator()

    # var_dat = {
    #     1: [1200, 1690, 5250],
    #     2: [9410, 13110, 16690],
    #     3: [20940, 24540, 28990],
    #     4: [32340, 35960, 39960],
    #     5: [42880, 47610, 51290],
    #     6: [55330, 59000, 61910],
    # }
    var_dat = {
        1: -270,
        2: 11196,
        3: 22598,
        4: 34055,
        5: 45449,
        6: 56951,
    }
    
    var_temp = calc.kclka_locator(var_dat)
    print(var_temp)

if __name__ == "__main__":
    main()