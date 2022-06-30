import json

from masterservice.service.goalmappingservice import GoalMappingService


class AppraisalDetailResponse:
    id, appraisal_id, remarks, rating, goal_mapping = (None,) * 5


    def get(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def set_id(self, id):
        self.id = id

    def set_appraisal_id(self, appraisal_id):
        self.appraisal_id = appraisal_id

    def set_remarks(self, remarks):
        self.remarks = remarks

    def set_rating(self, rating):
        self.rating = rating

    def set_goal_mapping(self, goal_mapping):
        goal_mapping_serv = GoalMappingService()
        val = goal_mapping_serv.get_goal_mapping(goal_mapping)
        self.goal_mapping = val