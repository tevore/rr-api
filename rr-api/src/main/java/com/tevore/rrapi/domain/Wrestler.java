package com.tevore.rrapi.domain;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.neo4j.core.schema.*;

import java.util.List;

@Node("Wrestler")
@Getter
@Setter
@ToString
public class Wrestler {

    @Id
    private Long id;

    @Property("name")
    private String name;

    @Relationship(type = "WON")
    private List<Event> eventsWon;


    public Wrestler(String name) {
        this.name = name;
    }
}
