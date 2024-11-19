def bouncing_ball(h, bounce, window):
    altura = h 
    if h <= 0 or not 0 < bounce < 1 or window >= altura:
          return -1
    
    rebotes = 1
    altura *= bounce
    while altura > window:
          rebotes += 2
          altura *= bounce
    return rebotes

if __name__ == "__main__":
        assert bouncing_ball(2, 0.5, 1) == 1
        assert bouncing_ball(3, 0.66, 1.5) == 3
        assert bouncing_ball(30, 0.66, 1.5) == 15
        assert bouncing_ball(30, 0.75, 1.5) == 21