import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API Call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)


# Store API response in a variable.
response_dict = r.json()
print("Total Repositories: ", response_dict['total_count'])

# Explore Information about the repositories
repo_dicts = response_dict['items']

names,plot_dicts = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	description = repo_dict['description']
	if not description:
		description = 'No description provided.'
	
	plot_dict = {
				'value' : repo_dict['stargazers_count'],
				'label' : description,
				'xlink' : repo_dict['html_url'],
				}
				
	plot_dicts.append(plot_dict)


my_style = LS('#333366', base_style = LCS)
chart =pygal.Bar(style = my_style,x_label_rotation=45,show_legend=False)
chart.title = 'Most-starred Python Projects on GitHub'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
