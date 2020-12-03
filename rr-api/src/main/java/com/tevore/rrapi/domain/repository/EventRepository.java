package com.tevore.rrapi.domain.repository;

import com.tevore.rrapi.domain.Event;
import org.springframework.data.neo4j.repository.Neo4jRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EventRepository extends Neo4jRepository<Event, Long> {
}
