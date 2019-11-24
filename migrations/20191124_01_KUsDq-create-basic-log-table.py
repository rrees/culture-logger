"""
Create basic log table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""CREATE TABLE culture_log (
		id serial,
		title text,
		content text,
		tags text[],
		rating smallint,
		category text,
		url text,
		bechdel_test boolean default false,
		violence_against_women boolean default false,
		created timestamp default current_timestamp,
		updated timestamp default current_timestamp
	)"""),

	step("""CREATE OR REPLACE FUNCTION update_modified_column() 
		RETURNS TRIGGER AS $$
		BEGIN
		    NEW.modified = now();
		    RETURN NEW; 
		END;
		$$ language 'plpgsql';

		CREATE TRIGGER update_log_modtime BEFORE UPDATE ON culture_log FOR EACH ROW EXECUTE PROCEDURE  update_modified_column();
	"""),
]
