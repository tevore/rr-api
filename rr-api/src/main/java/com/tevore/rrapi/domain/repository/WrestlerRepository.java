package com.tevore.rrapi.domain.repository;

import com.tevore.rrapi.domain.Wrestler;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.data.neo4j.repository.query.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface WrestlerRepository extends Neo4jRepository<Wrestler, Long> {
    Wrestler findByName(String name);

    //TODO enhance to bring back distinct + which rumbles they actually won
    @Query("MATCH (w:Wrestler)-[rel:WON]->(e:Event) return w, collect(rel), collect(e)")
    List<Wrestler> findAllWinners();

}
