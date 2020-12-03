package com.tevore.rrapi.web;

import com.tevore.rrapi.domain.Wrestler;
import com.tevore.rrapi.service.WrestlerDataService;
import com.tevore.rrapi.web.request.WrestlerRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
public class RRController {

    private WrestlerDataService wrestlerDataService;

    @Autowired
    public RRController(WrestlerDataService wrestlerDataService) {
        this.wrestlerDataService = wrestlerDataService;
    }

    @PostMapping("/find")
    public Wrestler findWrestler(@RequestBody WrestlerRequest request) {
        Wrestler w = wrestlerDataService.findWrestler(request.getName());
        //System.out.println(w.getName());
        return w;
    }

    @GetMapping("/winners")
    public List<Wrestler> findWinners() {
        return wrestlerDataService.findWinners();
    }
}
