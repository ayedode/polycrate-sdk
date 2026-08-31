from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_maintenances_partial_update_actual_availability_error_component import (
        ApiV1MaintenancesPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_additional_recipients_error_component import (
        ApiV1MaintenancesPartialUpdateAdditionalRecipientsErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_affected_host_ids_error_component import (
        ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_affected_pop_ids_error_component import (
        ApiV1MaintenancesPartialUpdateAffectedPopIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_affected_volume_ids_error_component import (
        ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_annotations_error_component import (
        ApiV1MaintenancesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_announcement_results_error_component import (
        ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_announcement_sent_error_component import (
        ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_archived_at_error_component import (
        ApiV1MaintenancesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_archived_by_error_component import (
        ApiV1MaintenancesPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_archived_error_component import (
        ApiV1MaintenancesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_archived_reason_error_component import (
        ApiV1MaintenancesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_created_by_component_error_component import (
        ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_created_by_user_error_component import (
        ApiV1MaintenancesPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_criticality_error_component import (
        ApiV1MaintenancesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_debug_mode_error_component import (
        ApiV1MaintenancesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_discovery_enabled_error_component import (
        ApiV1MaintenancesPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_display_name_error_component import (
        ApiV1MaintenancesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_draft_error_component import (
        ApiV1MaintenancesPartialUpdateDraftErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_end_announcement_sent_error_component import (
        ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_end_error_component import (
        ApiV1MaintenancesPartialUpdateEndErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_kind_error_component import (
        ApiV1MaintenancesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_labels_error_component import (
        ApiV1MaintenancesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1MaintenancesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_managed_by_content_type_error_component import (
        ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_managed_by_object_id_error_component import (
        ApiV1MaintenancesPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_modified_by_user_error_component import (
        ApiV1MaintenancesPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_name_error_component import (
        ApiV1MaintenancesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_non_field_errors_error_component import (
        ApiV1MaintenancesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_notification_ended_sent_error_component import (
        ApiV1MaintenancesPartialUpdateNotificationEndedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_notification_scheduled_sent_error_component import (
        ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_notification_started_sent_error_component import (
        ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_organization_id_error_component import (
        ApiV1MaintenancesPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_platform_dns_record_created_error_component import (
        ApiV1MaintenancesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_platform_service_error_component import (
        ApiV1MaintenancesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_project_id_error_component import (
        ApiV1MaintenancesPartialUpdateProjectIdErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_provider_entity_error_component import (
        ApiV1MaintenancesPartialUpdateProviderEntityErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_provider_error_component import (
        ApiV1MaintenancesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_provider_id_error_component import (
        ApiV1MaintenancesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_provider_reference_error_component import (
        ApiV1MaintenancesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_reconciliation_enabled_error_component import (
        ApiV1MaintenancesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_reference_url_error_component import (
        ApiV1MaintenancesPartialUpdateReferenceUrlErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_scope_error_component import (
        ApiV1MaintenancesPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_sla_availability_error_component import (
        ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_sla_target_error_component import (
        ApiV1MaintenancesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_sla_window_days_error_component import (
        ApiV1MaintenancesPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_slo_availability_error_component import (
        ApiV1MaintenancesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_slo_target_error_component import (
        ApiV1MaintenancesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_slo_window_days_error_component import (
        ApiV1MaintenancesPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_source_datasource_error_component import (
        ApiV1MaintenancesPartialUpdateSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_source_item_id_error_component import (
        ApiV1MaintenancesPartialUpdateSourceItemIdErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_start_announcement_sent_error_component import (
        ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_start_error_component import (
        ApiV1MaintenancesPartialUpdateStartErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_target_availability_error_component import (
        ApiV1MaintenancesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_timeline_error_component import (
        ApiV1MaintenancesPartialUpdateTimelineErrorComponent,
    )
    from ..models.api_v1_maintenances_partial_update_workspace_id_error_component import (
        ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1MaintenancesPartialUpdateValidationError")


@_attrs_define
class ApiV1MaintenancesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1MaintenancesPartialUpdateActualAvailabilityErrorComponent |
            ApiV1MaintenancesPartialUpdateAdditionalRecipientsErrorComponent |
            ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponent |
            ApiV1MaintenancesPartialUpdateAffectedPopIdsErrorComponent |
            ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponent |
            ApiV1MaintenancesPartialUpdateAnnotationsErrorComponent |
            ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponent |
            ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponent |
            ApiV1MaintenancesPartialUpdateArchivedAtErrorComponent | ApiV1MaintenancesPartialUpdateArchivedByErrorComponent
            | ApiV1MaintenancesPartialUpdateArchivedErrorComponent |
            ApiV1MaintenancesPartialUpdateArchivedReasonErrorComponent |
            ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponent |
            ApiV1MaintenancesPartialUpdateCreatedByUserErrorComponent |
            ApiV1MaintenancesPartialUpdateCriticalityErrorComponent | ApiV1MaintenancesPartialUpdateDebugModeErrorComponent
            | ApiV1MaintenancesPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1MaintenancesPartialUpdateDisplayNameErrorComponent | ApiV1MaintenancesPartialUpdateDraftErrorComponent |
            ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponent |
            ApiV1MaintenancesPartialUpdateEndErrorComponent | ApiV1MaintenancesPartialUpdateKindErrorComponent |
            ApiV1MaintenancesPartialUpdateLabelsErrorComponent |
            ApiV1MaintenancesPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1MaintenancesPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1MaintenancesPartialUpdateModifiedByUserErrorComponent | ApiV1MaintenancesPartialUpdateNameErrorComponent |
            ApiV1MaintenancesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1MaintenancesPartialUpdateNotificationEndedSentErrorComponent |
            ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponent |
            ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponent |
            ApiV1MaintenancesPartialUpdateOrganizationIdErrorComponent |
            ApiV1MaintenancesPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1MaintenancesPartialUpdatePlatformServiceErrorComponent |
            ApiV1MaintenancesPartialUpdateProjectIdErrorComponent |
            ApiV1MaintenancesPartialUpdateProviderEntityErrorComponent |
            ApiV1MaintenancesPartialUpdateProviderErrorComponent | ApiV1MaintenancesPartialUpdateProviderIdErrorComponent |
            ApiV1MaintenancesPartialUpdateProviderReferenceErrorComponent |
            ApiV1MaintenancesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1MaintenancesPartialUpdateReferenceUrlErrorComponent | ApiV1MaintenancesPartialUpdateScopeErrorComponent |
            ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1MaintenancesPartialUpdateSlaTargetErrorComponent |
            ApiV1MaintenancesPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1MaintenancesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1MaintenancesPartialUpdateSloTargetErrorComponent |
            ApiV1MaintenancesPartialUpdateSloWindowDaysErrorComponent |
            ApiV1MaintenancesPartialUpdateSourceDatasourceErrorComponent |
            ApiV1MaintenancesPartialUpdateSourceItemIdErrorComponent |
            ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponent |
            ApiV1MaintenancesPartialUpdateStartErrorComponent |
            ApiV1MaintenancesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1MaintenancesPartialUpdateTimelineErrorComponent |
            ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1MaintenancesPartialUpdateActualAvailabilityErrorComponent
        | ApiV1MaintenancesPartialUpdateAdditionalRecipientsErrorComponent
        | ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponent
        | ApiV1MaintenancesPartialUpdateAffectedPopIdsErrorComponent
        | ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponent
        | ApiV1MaintenancesPartialUpdateAnnotationsErrorComponent
        | ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponent
        | ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponent
        | ApiV1MaintenancesPartialUpdateArchivedAtErrorComponent
        | ApiV1MaintenancesPartialUpdateArchivedByErrorComponent
        | ApiV1MaintenancesPartialUpdateArchivedErrorComponent
        | ApiV1MaintenancesPartialUpdateArchivedReasonErrorComponent
        | ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponent
        | ApiV1MaintenancesPartialUpdateCreatedByUserErrorComponent
        | ApiV1MaintenancesPartialUpdateCriticalityErrorComponent
        | ApiV1MaintenancesPartialUpdateDebugModeErrorComponent
        | ApiV1MaintenancesPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1MaintenancesPartialUpdateDisplayNameErrorComponent
        | ApiV1MaintenancesPartialUpdateDraftErrorComponent
        | ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponent
        | ApiV1MaintenancesPartialUpdateEndErrorComponent
        | ApiV1MaintenancesPartialUpdateKindErrorComponent
        | ApiV1MaintenancesPartialUpdateLabelsErrorComponent
        | ApiV1MaintenancesPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1MaintenancesPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1MaintenancesPartialUpdateModifiedByUserErrorComponent
        | ApiV1MaintenancesPartialUpdateNameErrorComponent
        | ApiV1MaintenancesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1MaintenancesPartialUpdateNotificationEndedSentErrorComponent
        | ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponent
        | ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponent
        | ApiV1MaintenancesPartialUpdateOrganizationIdErrorComponent
        | ApiV1MaintenancesPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1MaintenancesPartialUpdatePlatformServiceErrorComponent
        | ApiV1MaintenancesPartialUpdateProjectIdErrorComponent
        | ApiV1MaintenancesPartialUpdateProviderEntityErrorComponent
        | ApiV1MaintenancesPartialUpdateProviderErrorComponent
        | ApiV1MaintenancesPartialUpdateProviderIdErrorComponent
        | ApiV1MaintenancesPartialUpdateProviderReferenceErrorComponent
        | ApiV1MaintenancesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1MaintenancesPartialUpdateReferenceUrlErrorComponent
        | ApiV1MaintenancesPartialUpdateScopeErrorComponent
        | ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1MaintenancesPartialUpdateSlaTargetErrorComponent
        | ApiV1MaintenancesPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1MaintenancesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1MaintenancesPartialUpdateSloTargetErrorComponent
        | ApiV1MaintenancesPartialUpdateSloWindowDaysErrorComponent
        | ApiV1MaintenancesPartialUpdateSourceDatasourceErrorComponent
        | ApiV1MaintenancesPartialUpdateSourceItemIdErrorComponent
        | ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponent
        | ApiV1MaintenancesPartialUpdateStartErrorComponent
        | ApiV1MaintenancesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1MaintenancesPartialUpdateTimelineErrorComponent
        | ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_maintenances_partial_update_actual_availability_error_component import (
            ApiV1MaintenancesPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_additional_recipients_error_component import (
            ApiV1MaintenancesPartialUpdateAdditionalRecipientsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_affected_host_ids_error_component import (
            ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_affected_pop_ids_error_component import (
            ApiV1MaintenancesPartialUpdateAffectedPopIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_affected_volume_ids_error_component import (
            ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_annotations_error_component import (
            ApiV1MaintenancesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_announcement_results_error_component import (
            ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_announcement_sent_error_component import (
            ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_archived_at_error_component import (
            ApiV1MaintenancesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_archived_by_error_component import (
            ApiV1MaintenancesPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_archived_error_component import (
            ApiV1MaintenancesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_archived_reason_error_component import (
            ApiV1MaintenancesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_created_by_component_error_component import (
            ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_created_by_user_error_component import (
            ApiV1MaintenancesPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_criticality_error_component import (
            ApiV1MaintenancesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_debug_mode_error_component import (
            ApiV1MaintenancesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_discovery_enabled_error_component import (
            ApiV1MaintenancesPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_display_name_error_component import (
            ApiV1MaintenancesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_draft_error_component import (
            ApiV1MaintenancesPartialUpdateDraftErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_end_announcement_sent_error_component import (
            ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_end_error_component import (
            ApiV1MaintenancesPartialUpdateEndErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_kind_error_component import (
            ApiV1MaintenancesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_labels_error_component import (
            ApiV1MaintenancesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_managed_by_content_type_error_component import (
            ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_managed_by_object_id_error_component import (
            ApiV1MaintenancesPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_modified_by_user_error_component import (
            ApiV1MaintenancesPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_name_error_component import (
            ApiV1MaintenancesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_non_field_errors_error_component import (
            ApiV1MaintenancesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_notification_ended_sent_error_component import (
            ApiV1MaintenancesPartialUpdateNotificationEndedSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_notification_started_sent_error_component import (
            ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_organization_id_error_component import (
            ApiV1MaintenancesPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_platform_dns_record_created_error_component import (
            ApiV1MaintenancesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_platform_service_error_component import (
            ApiV1MaintenancesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_project_id_error_component import (
            ApiV1MaintenancesPartialUpdateProjectIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_provider_entity_error_component import (
            ApiV1MaintenancesPartialUpdateProviderEntityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_provider_error_component import (
            ApiV1MaintenancesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_provider_id_error_component import (
            ApiV1MaintenancesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_provider_reference_error_component import (
            ApiV1MaintenancesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_reconciliation_enabled_error_component import (
            ApiV1MaintenancesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_reference_url_error_component import (
            ApiV1MaintenancesPartialUpdateReferenceUrlErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_scope_error_component import (
            ApiV1MaintenancesPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_sla_availability_error_component import (
            ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_sla_target_error_component import (
            ApiV1MaintenancesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_sla_window_days_error_component import (
            ApiV1MaintenancesPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_slo_availability_error_component import (
            ApiV1MaintenancesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_slo_target_error_component import (
            ApiV1MaintenancesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_slo_window_days_error_component import (
            ApiV1MaintenancesPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_source_item_id_error_component import (
            ApiV1MaintenancesPartialUpdateSourceItemIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_start_announcement_sent_error_component import (
            ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_start_error_component import (
            ApiV1MaintenancesPartialUpdateStartErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_target_availability_error_component import (
            ApiV1MaintenancesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_timeline_error_component import (
            ApiV1MaintenancesPartialUpdateTimelineErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_workspace_id_error_component import (
            ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateProjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateAffectedPopIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1MaintenancesPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateSourceItemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateReferenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateAdditionalRecipientsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateTimelineErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateNotificationEndedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1MaintenancesPartialUpdateProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_maintenances_partial_update_actual_availability_error_component import (
            ApiV1MaintenancesPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_additional_recipients_error_component import (
            ApiV1MaintenancesPartialUpdateAdditionalRecipientsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_affected_host_ids_error_component import (
            ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_affected_pop_ids_error_component import (
            ApiV1MaintenancesPartialUpdateAffectedPopIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_affected_volume_ids_error_component import (
            ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_annotations_error_component import (
            ApiV1MaintenancesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_announcement_results_error_component import (
            ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_announcement_sent_error_component import (
            ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_archived_at_error_component import (
            ApiV1MaintenancesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_archived_by_error_component import (
            ApiV1MaintenancesPartialUpdateArchivedByErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_archived_error_component import (
            ApiV1MaintenancesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_archived_reason_error_component import (
            ApiV1MaintenancesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_created_by_component_error_component import (
            ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_created_by_user_error_component import (
            ApiV1MaintenancesPartialUpdateCreatedByUserErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_criticality_error_component import (
            ApiV1MaintenancesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_debug_mode_error_component import (
            ApiV1MaintenancesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_discovery_enabled_error_component import (
            ApiV1MaintenancesPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_display_name_error_component import (
            ApiV1MaintenancesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_draft_error_component import (
            ApiV1MaintenancesPartialUpdateDraftErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_end_announcement_sent_error_component import (
            ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_end_error_component import (
            ApiV1MaintenancesPartialUpdateEndErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_kind_error_component import (
            ApiV1MaintenancesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_labels_error_component import (
            ApiV1MaintenancesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1MaintenancesPartialUpdateLastReconciliationDurationSecondsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_managed_by_content_type_error_component import (
            ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_managed_by_object_id_error_component import (
            ApiV1MaintenancesPartialUpdateManagedByObjectIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_modified_by_user_error_component import (
            ApiV1MaintenancesPartialUpdateModifiedByUserErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_name_error_component import (
            ApiV1MaintenancesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_non_field_errors_error_component import (
            ApiV1MaintenancesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_notification_ended_sent_error_component import (
            ApiV1MaintenancesPartialUpdateNotificationEndedSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_notification_scheduled_sent_error_component import (
            ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_notification_started_sent_error_component import (
            ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_organization_id_error_component import (
            ApiV1MaintenancesPartialUpdateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_platform_dns_record_created_error_component import (
            ApiV1MaintenancesPartialUpdatePlatformDnsRecordCreatedErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_platform_service_error_component import (
            ApiV1MaintenancesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_project_id_error_component import (
            ApiV1MaintenancesPartialUpdateProjectIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_provider_entity_error_component import (
            ApiV1MaintenancesPartialUpdateProviderEntityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_provider_error_component import (
            ApiV1MaintenancesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_provider_id_error_component import (
            ApiV1MaintenancesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_provider_reference_error_component import (
            ApiV1MaintenancesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_reconciliation_enabled_error_component import (
            ApiV1MaintenancesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_reference_url_error_component import (
            ApiV1MaintenancesPartialUpdateReferenceUrlErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_scope_error_component import (
            ApiV1MaintenancesPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_sla_availability_error_component import (
            ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_sla_target_error_component import (
            ApiV1MaintenancesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_sla_window_days_error_component import (
            ApiV1MaintenancesPartialUpdateSlaWindowDaysErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_slo_availability_error_component import (
            ApiV1MaintenancesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_slo_target_error_component import (
            ApiV1MaintenancesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_slo_window_days_error_component import (
            ApiV1MaintenancesPartialUpdateSloWindowDaysErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_source_datasource_error_component import (
            ApiV1MaintenancesPartialUpdateSourceDatasourceErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_source_item_id_error_component import (
            ApiV1MaintenancesPartialUpdateSourceItemIdErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_start_announcement_sent_error_component import (
            ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_start_error_component import (
            ApiV1MaintenancesPartialUpdateStartErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_target_availability_error_component import (
            ApiV1MaintenancesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_timeline_error_component import (
            ApiV1MaintenancesPartialUpdateTimelineErrorComponent,
        )
        from ..models.api_v1_maintenances_partial_update_workspace_id_error_component import (
            ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1MaintenancesPartialUpdateActualAvailabilityErrorComponent
                | ApiV1MaintenancesPartialUpdateAdditionalRecipientsErrorComponent
                | ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponent
                | ApiV1MaintenancesPartialUpdateAffectedPopIdsErrorComponent
                | ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponent
                | ApiV1MaintenancesPartialUpdateAnnotationsErrorComponent
                | ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponent
                | ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponent
                | ApiV1MaintenancesPartialUpdateArchivedAtErrorComponent
                | ApiV1MaintenancesPartialUpdateArchivedByErrorComponent
                | ApiV1MaintenancesPartialUpdateArchivedErrorComponent
                | ApiV1MaintenancesPartialUpdateArchivedReasonErrorComponent
                | ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponent
                | ApiV1MaintenancesPartialUpdateCreatedByUserErrorComponent
                | ApiV1MaintenancesPartialUpdateCriticalityErrorComponent
                | ApiV1MaintenancesPartialUpdateDebugModeErrorComponent
                | ApiV1MaintenancesPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1MaintenancesPartialUpdateDisplayNameErrorComponent
                | ApiV1MaintenancesPartialUpdateDraftErrorComponent
                | ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponent
                | ApiV1MaintenancesPartialUpdateEndErrorComponent
                | ApiV1MaintenancesPartialUpdateKindErrorComponent
                | ApiV1MaintenancesPartialUpdateLabelsErrorComponent
                | ApiV1MaintenancesPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1MaintenancesPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1MaintenancesPartialUpdateModifiedByUserErrorComponent
                | ApiV1MaintenancesPartialUpdateNameErrorComponent
                | ApiV1MaintenancesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1MaintenancesPartialUpdateNotificationEndedSentErrorComponent
                | ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponent
                | ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponent
                | ApiV1MaintenancesPartialUpdateOrganizationIdErrorComponent
                | ApiV1MaintenancesPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1MaintenancesPartialUpdatePlatformServiceErrorComponent
                | ApiV1MaintenancesPartialUpdateProjectIdErrorComponent
                | ApiV1MaintenancesPartialUpdateProviderEntityErrorComponent
                | ApiV1MaintenancesPartialUpdateProviderErrorComponent
                | ApiV1MaintenancesPartialUpdateProviderIdErrorComponent
                | ApiV1MaintenancesPartialUpdateProviderReferenceErrorComponent
                | ApiV1MaintenancesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1MaintenancesPartialUpdateReferenceUrlErrorComponent
                | ApiV1MaintenancesPartialUpdateScopeErrorComponent
                | ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1MaintenancesPartialUpdateSlaTargetErrorComponent
                | ApiV1MaintenancesPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1MaintenancesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1MaintenancesPartialUpdateSloTargetErrorComponent
                | ApiV1MaintenancesPartialUpdateSloWindowDaysErrorComponent
                | ApiV1MaintenancesPartialUpdateSourceDatasourceErrorComponent
                | ApiV1MaintenancesPartialUpdateSourceItemIdErrorComponent
                | ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponent
                | ApiV1MaintenancesPartialUpdateStartErrorComponent
                | ApiV1MaintenancesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1MaintenancesPartialUpdateTimelineErrorComponent
                | ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_0 = (
                        ApiV1MaintenancesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_1 = (
                        ApiV1MaintenancesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_2 = (
                        ApiV1MaintenancesPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_3 = (
                        ApiV1MaintenancesPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_4 = (
                        ApiV1MaintenancesPartialUpdateProjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_5 = (
                        ApiV1MaintenancesPartialUpdateAffectedHostIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_6 = (
                        ApiV1MaintenancesPartialUpdateAffectedVolumeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_7 = (
                        ApiV1MaintenancesPartialUpdateAffectedPopIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_8 = (
                        ApiV1MaintenancesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_9 = (
                        ApiV1MaintenancesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_10 = (
                        ApiV1MaintenancesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_11 = (
                        ApiV1MaintenancesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_12 = (
                        ApiV1MaintenancesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_13 = (
                        ApiV1MaintenancesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_14 = (
                        ApiV1MaintenancesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_15 = (
                        ApiV1MaintenancesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_16 = (
                        ApiV1MaintenancesPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_17 = (
                        ApiV1MaintenancesPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_18 = (
                        ApiV1MaintenancesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_19 = (
                        ApiV1MaintenancesPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_20 = (
                        ApiV1MaintenancesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_21 = (
                        ApiV1MaintenancesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_22 = (
                        ApiV1MaintenancesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_23 = (
                        ApiV1MaintenancesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_24 = (
                        ApiV1MaintenancesPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_25 = (
                        ApiV1MaintenancesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_26 = (
                        ApiV1MaintenancesPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_27 = (
                        ApiV1MaintenancesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_28 = (
                        ApiV1MaintenancesPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_29 = (
                        ApiV1MaintenancesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_30 = (
                        ApiV1MaintenancesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_31 = (
                        ApiV1MaintenancesPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_32 = (
                        ApiV1MaintenancesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_33 = (
                        ApiV1MaintenancesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_34 = (
                        ApiV1MaintenancesPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_35 = (
                        ApiV1MaintenancesPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_36 = (
                        ApiV1MaintenancesPartialUpdateStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_37 = (
                        ApiV1MaintenancesPartialUpdateEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_38 = (
                        ApiV1MaintenancesPartialUpdateDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_39 = (
                        ApiV1MaintenancesPartialUpdateSourceItemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_40 = (
                        ApiV1MaintenancesPartialUpdateReferenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_41 = (
                        ApiV1MaintenancesPartialUpdateAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_42 = (
                        ApiV1MaintenancesPartialUpdateStartAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_43 = (
                        ApiV1MaintenancesPartialUpdateEndAnnouncementSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_44 = (
                        ApiV1MaintenancesPartialUpdateAdditionalRecipientsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_45 = (
                        ApiV1MaintenancesPartialUpdateAnnouncementResultsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_46 = (
                        ApiV1MaintenancesPartialUpdateTimelineErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_47 = (
                        ApiV1MaintenancesPartialUpdateNotificationScheduledSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_48 = (
                        ApiV1MaintenancesPartialUpdateNotificationStartedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_49 = (
                        ApiV1MaintenancesPartialUpdateNotificationEndedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_50 = (
                        ApiV1MaintenancesPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_51 = (
                        ApiV1MaintenancesPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_51
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_52 = (
                        ApiV1MaintenancesPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_52
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_53 = (
                        ApiV1MaintenancesPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_53
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_maintenances_partial_update_error_type_54 = (
                        ApiV1MaintenancesPartialUpdateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_maintenances_partial_update_error_type_54
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_maintenances_partial_update_error_type_55 = (
                    ApiV1MaintenancesPartialUpdateSourceDatasourceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_maintenances_partial_update_error_type_55

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_maintenances_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_maintenances_partial_update_validation_error.additional_properties = d
        return api_v1_maintenances_partial_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
