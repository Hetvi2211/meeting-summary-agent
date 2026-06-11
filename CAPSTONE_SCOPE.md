# Capstone Scope Document

## Project

Meeting Summary Agent

## Feature

Summary History

## Problem Statement

Users can generate meeting summaries, but they cannot view previously generated summaries.

## User Story

As a user, I want to view previous meeting summaries so that I can refer to past meetings without generating them again.

## Scope

* Save summaries to SQLite database
* Create History page
* Display previous summaries
* Show latest summaries first

## Out of Scope

* Editing summaries
* Deleting summaries
* User authentication

## Test Plan

1. Generate a summary
2. Verify it is saved in SQLite
3. Open History page
4. Verify summary appears
5. Generate another summary
6. Verify both summaries are visible

## Success Criteria

* Summaries are stored successfully
* History page loads correctly
* Latest summaries appear first
