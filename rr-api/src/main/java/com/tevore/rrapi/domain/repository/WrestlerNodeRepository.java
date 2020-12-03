package com.tevore.rrapi.domain.repository;

import com.tevore.rrapi.domain.Wrestler;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface WrestlerNodeRepository extends Neo4jRepository<Wrestler, Long> {
    Wrestler findByName(String name);
}
