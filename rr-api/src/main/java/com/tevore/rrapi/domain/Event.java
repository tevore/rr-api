package com.tevore.rrapi.domain;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;
import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;
import org.springframework.data.neo4j.core.schema.Property;
import org.springframework.data.neo4j.core.schema.Relationship;

import java.util.List;

@Node("Event")
@Getter
@Setter
@ToString
public class Event {

    @Id
    private Long id;

    @Property("name")
    private String name;

    @Property("year")
    private Integer year;

    @Relationship(type = "WON", direction = Relationship.Direction.INCOMING)
    private List<Wrestler> winners;


    private List<Wrestler> participants;

    public Event(String name, Integer year) {
        this.name = name;
        this.year = year;
    }
    

}
