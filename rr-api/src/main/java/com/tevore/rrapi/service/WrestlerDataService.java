package com.tevore.rrapi.service;

import com.tevore.rrapi.domain.Wrestler;
import com.tevore.rrapi.domain.repository.WrestlerNodeRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class WrestlerDataService {

    private final Logger LOGGER = LoggerFactory.getLogger(WrestlerDataService.class);

    private WrestlerNodeRepository wrestlerNodeRepository;

    @Autowired
    public WrestlerDataService(WrestlerNodeRepository wrestlerNodeRepository) {
        this.wrestlerNodeRepository = wrestlerNodeRepository;
    }

    public Wrestler findWrestler(String name) {
        LOGGER.info("Looking for wrestler {}", name);
        return wrestlerNodeRepository.findByName(name);
    }

    public List<Wrestler> findWinners() {

        LOGGER.info("Gathering all rumble winners...");
        return wrestlerNodeRepository.findAllWinners();
    }
}
