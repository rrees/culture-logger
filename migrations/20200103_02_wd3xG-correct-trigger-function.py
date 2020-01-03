"""
Correct trigger function
"""

from yoyo import step

__depends__ = {'20200103_01_hUxGf-adds-an-explicit-log-date'}

steps = [
	step("""CREATE OR REPLACE FUNCTION update_modified_column() 
		RETURNS TRIGGER AS $$
		BEGIN
		    NEW.updated = now();
		    RETURN NEW; 
		END;
		$$ language 'plpgsql';""")
]
