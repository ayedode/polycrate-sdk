from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_incidents_partial_update_actual_availability_error_component import (
        ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_affected_host_ids_error_component import (
        ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_affected_pop_ids_error_component import (
        ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_affected_volume_ids_error_component import (
        ApiV1IncidentsPartialUpdateAffectedVolumeIdsErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_annotations_error_component import (
        ApiV1IncidentsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_archived_at_error_component import (
        ApiV1IncidentsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_archived_by_error_component import (
        ApiV1IncidentsPartialUpdateArchivedByErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_archived_error_component import (
        ApiV1IncidentsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_archived_reason_error_component import (
        ApiV1IncidentsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_created_by_component_error_component import (
        ApiV1IncidentsPartialUpdateCreatedByComponentErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_created_by_user_error_component import (
        ApiV1IncidentsPartialUpdateCreatedByUserErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_criticality_error_component import (
        ApiV1IncidentsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_debug_mode_error_component import (
        ApiV1IncidentsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_discovered_at_error_component import (
        ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_discovery_enabled_error_component import (
        ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_display_name_error_component import (
        ApiV1IncidentsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_downtime_ids_error_component import (
        ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_kind_error_component import (
        ApiV1IncidentsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_labels_error_component import (
        ApiV1IncidentsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_last_reconciliation_duration_seconds_error_component import (
        ApiV1IncidentsPartialUpdateLastReconciliationDurationSecondsErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_managed_by_content_type_error_component import (
        ApiV1IncidentsPartialUpdateManagedByContentTypeErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_managed_by_object_id_error_component import (
        ApiV1IncidentsPartialUpdateManagedByObjectIdErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_modified_by_user_error_component import (
        ApiV1IncidentsPartialUpdateModifiedByUserErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_name_error_component import (
        ApiV1IncidentsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_non_field_errors_error_component import (
        ApiV1IncidentsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_notification_closed_sent_error_component import (
        ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_notification_opened_sent_error_component import (
        ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_occurred_at_error_component import (
        ApiV1IncidentsPartialUpdateOccurredAtErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_organization_id_error_component import (
        ApiV1IncidentsPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_platform_dns_record_created_error_component import (
        ApiV1IncidentsPartialUpdatePlatformDnsRecordCreatedErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_platform_service_error_component import (
        ApiV1IncidentsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_provider_entity_error_component import (
        ApiV1IncidentsPartialUpdateProviderEntityErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_provider_error_component import (
        ApiV1IncidentsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_provider_id_error_component import (
        ApiV1IncidentsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_provider_reference_error_component import (
        ApiV1IncidentsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_reconciliation_enabled_error_component import (
        ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_reference_url_error_component import (
        ApiV1IncidentsPartialUpdateReferenceUrlErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_reporter_error_component import (
        ApiV1IncidentsPartialUpdateReporterErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_resolved_at_error_component import (
        ApiV1IncidentsPartialUpdateResolvedAtErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_scope_error_component import (
        ApiV1IncidentsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_sla_availability_error_component import (
        ApiV1IncidentsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_sla_target_error_component import (
        ApiV1IncidentsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_sla_window_days_error_component import (
        ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_slo_availability_error_component import (
        ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_slo_target_error_component import (
        ApiV1IncidentsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_slo_window_days_error_component import (
        ApiV1IncidentsPartialUpdateSloWindowDaysErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_source_datasource_error_component import (
        ApiV1IncidentsPartialUpdateSourceDatasourceErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_source_item_id_error_component import (
        ApiV1IncidentsPartialUpdateSourceItemIdErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_status_error_component import (
        ApiV1IncidentsPartialUpdateStatusErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_target_availability_error_component import (
        ApiV1IncidentsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_vulnerability_finding_ids_error_component import (
        ApiV1IncidentsPartialUpdateVulnerabilityFindingIdsErrorComponent,
    )
    from ..models.api_v1_incidents_partial_update_workspace_id_error_component import (
        ApiV1IncidentsPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1IncidentsPartialUpdateValidationError")


@_attrs_define
class ApiV1IncidentsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponent |
            ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponent |
            ApiV1IncidentsPartialUpdateAffectedVolumeIdsErrorComponent |
            ApiV1IncidentsPartialUpdateAnnotationsErrorComponent | ApiV1IncidentsPartialUpdateArchivedAtErrorComponent |
            ApiV1IncidentsPartialUpdateArchivedByErrorComponent | ApiV1IncidentsPartialUpdateArchivedErrorComponent |
            ApiV1IncidentsPartialUpdateArchivedReasonErrorComponent |
            ApiV1IncidentsPartialUpdateCreatedByComponentErrorComponent |
            ApiV1IncidentsPartialUpdateCreatedByUserErrorComponent | ApiV1IncidentsPartialUpdateCriticalityErrorComponent |
            ApiV1IncidentsPartialUpdateDebugModeErrorComponent | ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponent |
            ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponent | ApiV1IncidentsPartialUpdateDisplayNameErrorComponent
            | ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponent | ApiV1IncidentsPartialUpdateKindErrorComponent |
            ApiV1IncidentsPartialUpdateLabelsErrorComponent |
            ApiV1IncidentsPartialUpdateLastReconciliationDurationSecondsErrorComponent |
            ApiV1IncidentsPartialUpdateManagedByContentTypeErrorComponent |
            ApiV1IncidentsPartialUpdateManagedByObjectIdErrorComponent |
            ApiV1IncidentsPartialUpdateModifiedByUserErrorComponent | ApiV1IncidentsPartialUpdateNameErrorComponent |
            ApiV1IncidentsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponent |
            ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponent |
            ApiV1IncidentsPartialUpdateOccurredAtErrorComponent | ApiV1IncidentsPartialUpdateOrganizationIdErrorComponent |
            ApiV1IncidentsPartialUpdatePlatformDnsRecordCreatedErrorComponent |
            ApiV1IncidentsPartialUpdatePlatformServiceErrorComponent |
            ApiV1IncidentsPartialUpdateProviderEntityErrorComponent | ApiV1IncidentsPartialUpdateProviderErrorComponent |
            ApiV1IncidentsPartialUpdateProviderIdErrorComponent | ApiV1IncidentsPartialUpdateProviderReferenceErrorComponent
            | ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1IncidentsPartialUpdateReferenceUrlErrorComponent | ApiV1IncidentsPartialUpdateReporterErrorComponent |
            ApiV1IncidentsPartialUpdateResolvedAtErrorComponent | ApiV1IncidentsPartialUpdateScopeErrorComponent |
            ApiV1IncidentsPartialUpdateSlaAvailabilityErrorComponent | ApiV1IncidentsPartialUpdateSlaTargetErrorComponent |
            ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponent |
            ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponent | ApiV1IncidentsPartialUpdateSloTargetErrorComponent |
            ApiV1IncidentsPartialUpdateSloWindowDaysErrorComponent |
            ApiV1IncidentsPartialUpdateSourceDatasourceErrorComponent |
            ApiV1IncidentsPartialUpdateSourceItemIdErrorComponent | ApiV1IncidentsPartialUpdateStatusErrorComponent |
            ApiV1IncidentsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1IncidentsPartialUpdateVulnerabilityFindingIdsErrorComponent |
            ApiV1IncidentsPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponent
        | ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponent
        | ApiV1IncidentsPartialUpdateAffectedVolumeIdsErrorComponent
        | ApiV1IncidentsPartialUpdateAnnotationsErrorComponent
        | ApiV1IncidentsPartialUpdateArchivedAtErrorComponent
        | ApiV1IncidentsPartialUpdateArchivedByErrorComponent
        | ApiV1IncidentsPartialUpdateArchivedErrorComponent
        | ApiV1IncidentsPartialUpdateArchivedReasonErrorComponent
        | ApiV1IncidentsPartialUpdateCreatedByComponentErrorComponent
        | ApiV1IncidentsPartialUpdateCreatedByUserErrorComponent
        | ApiV1IncidentsPartialUpdateCriticalityErrorComponent
        | ApiV1IncidentsPartialUpdateDebugModeErrorComponent
        | ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponent
        | ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1IncidentsPartialUpdateDisplayNameErrorComponent
        | ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponent
        | ApiV1IncidentsPartialUpdateKindErrorComponent
        | ApiV1IncidentsPartialUpdateLabelsErrorComponent
        | ApiV1IncidentsPartialUpdateLastReconciliationDurationSecondsErrorComponent
        | ApiV1IncidentsPartialUpdateManagedByContentTypeErrorComponent
        | ApiV1IncidentsPartialUpdateManagedByObjectIdErrorComponent
        | ApiV1IncidentsPartialUpdateModifiedByUserErrorComponent
        | ApiV1IncidentsPartialUpdateNameErrorComponent
        | ApiV1IncidentsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponent
        | ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponent
        | ApiV1IncidentsPartialUpdateOccurredAtErrorComponent
        | ApiV1IncidentsPartialUpdateOrganizationIdErrorComponent
        | ApiV1IncidentsPartialUpdatePlatformDnsRecordCreatedErrorComponent
        | ApiV1IncidentsPartialUpdatePlatformServiceErrorComponent
        | ApiV1IncidentsPartialUpdateProviderEntityErrorComponent
        | ApiV1IncidentsPartialUpdateProviderErrorComponent
        | ApiV1IncidentsPartialUpdateProviderIdErrorComponent
        | ApiV1IncidentsPartialUpdateProviderReferenceErrorComponent
        | ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1IncidentsPartialUpdateReferenceUrlErrorComponent
        | ApiV1IncidentsPartialUpdateReporterErrorComponent
        | ApiV1IncidentsPartialUpdateResolvedAtErrorComponent
        | ApiV1IncidentsPartialUpdateScopeErrorComponent
        | ApiV1IncidentsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1IncidentsPartialUpdateSlaTargetErrorComponent
        | ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponent
        | ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1IncidentsPartialUpdateSloTargetErrorComponent
        | ApiV1IncidentsPartialUpdateSloWindowDaysErrorComponent
        | ApiV1IncidentsPartialUpdateSourceDatasourceErrorComponent
        | ApiV1IncidentsPartialUpdateSourceItemIdErrorComponent
        | ApiV1IncidentsPartialUpdateStatusErrorComponent
        | ApiV1IncidentsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1IncidentsPartialUpdateVulnerabilityFindingIdsErrorComponent
        | ApiV1IncidentsPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_incidents_partial_update_actual_availability_error_component import (
            ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_affected_host_ids_error_component import (
            ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_affected_pop_ids_error_component import (
            ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_affected_volume_ids_error_component import (
            ApiV1IncidentsPartialUpdateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_annotations_error_component import (
            ApiV1IncidentsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_archived_at_error_component import (
            ApiV1IncidentsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_archived_by_error_component import (
            ApiV1IncidentsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_archived_error_component import (
            ApiV1IncidentsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_archived_reason_error_component import (
            ApiV1IncidentsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_created_by_component_error_component import (
            ApiV1IncidentsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_created_by_user_error_component import (
            ApiV1IncidentsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_criticality_error_component import (
            ApiV1IncidentsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_debug_mode_error_component import (
            ApiV1IncidentsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_discovered_at_error_component import (
            ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_discovery_enabled_error_component import (
            ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_display_name_error_component import (
            ApiV1IncidentsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_downtime_ids_error_component import (
            ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_kind_error_component import (
            ApiV1IncidentsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_labels_error_component import (
            ApiV1IncidentsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1IncidentsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_managed_by_content_type_error_component import (
            ApiV1IncidentsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_managed_by_object_id_error_component import (
            ApiV1IncidentsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_modified_by_user_error_component import (
            ApiV1IncidentsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_name_error_component import (
            ApiV1IncidentsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_non_field_errors_error_component import (
            ApiV1IncidentsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_notification_closed_sent_error_component import (
            ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_notification_opened_sent_error_component import (
            ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_occurred_at_error_component import (
            ApiV1IncidentsPartialUpdateOccurredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_organization_id_error_component import (
            ApiV1IncidentsPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_platform_dns_record_created_error_component import (
            ApiV1IncidentsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_platform_service_error_component import (
            ApiV1IncidentsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_provider_entity_error_component import (
            ApiV1IncidentsPartialUpdateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_provider_error_component import (
            ApiV1IncidentsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_provider_id_error_component import (
            ApiV1IncidentsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_provider_reference_error_component import (
            ApiV1IncidentsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_reconciliation_enabled_error_component import (
            ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_reference_url_error_component import (
            ApiV1IncidentsPartialUpdateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_reporter_error_component import (
            ApiV1IncidentsPartialUpdateReporterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_resolved_at_error_component import (
            ApiV1IncidentsPartialUpdateResolvedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_scope_error_component import (
            ApiV1IncidentsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_sla_availability_error_component import (
            ApiV1IncidentsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_sla_target_error_component import (
            ApiV1IncidentsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_sla_window_days_error_component import (
            ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_slo_availability_error_component import (
            ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_slo_target_error_component import (
            ApiV1IncidentsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_slo_window_days_error_component import (
            ApiV1IncidentsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_source_item_id_error_component import (
            ApiV1IncidentsPartialUpdateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_status_error_component import (
            ApiV1IncidentsPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_target_availability_error_component import (
            ApiV1IncidentsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_vulnerability_finding_ids_error_component import (
            ApiV1IncidentsPartialUpdateVulnerabilityFindingIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_workspace_id_error_component import (
            ApiV1IncidentsPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1IncidentsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateAffectedVolumeIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateVulnerabilityFindingIdsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1IncidentsPartialUpdateLastReconciliationDurationSecondsErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateCreatedByComponentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateSloWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateManagedByObjectIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdatePlatformDnsRecordCreatedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateOccurredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateResolvedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateReporterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateReferenceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateSourceItemIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateArchivedByErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateManagedByContentTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateModifiedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateCreatedByUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1IncidentsPartialUpdateProviderEntityErrorComponent):
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
        from ..models.api_v1_incidents_partial_update_actual_availability_error_component import (
            ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_affected_host_ids_error_component import (
            ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_affected_pop_ids_error_component import (
            ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_affected_volume_ids_error_component import (
            ApiV1IncidentsPartialUpdateAffectedVolumeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_annotations_error_component import (
            ApiV1IncidentsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_archived_at_error_component import (
            ApiV1IncidentsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_archived_by_error_component import (
            ApiV1IncidentsPartialUpdateArchivedByErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_archived_error_component import (
            ApiV1IncidentsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_archived_reason_error_component import (
            ApiV1IncidentsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_created_by_component_error_component import (
            ApiV1IncidentsPartialUpdateCreatedByComponentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_created_by_user_error_component import (
            ApiV1IncidentsPartialUpdateCreatedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_criticality_error_component import (
            ApiV1IncidentsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_debug_mode_error_component import (
            ApiV1IncidentsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_discovered_at_error_component import (
            ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_discovery_enabled_error_component import (
            ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_display_name_error_component import (
            ApiV1IncidentsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_downtime_ids_error_component import (
            ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_kind_error_component import (
            ApiV1IncidentsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_labels_error_component import (
            ApiV1IncidentsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_last_reconciliation_duration_seconds_error_component import (
            ApiV1IncidentsPartialUpdateLastReconciliationDurationSecondsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_managed_by_content_type_error_component import (
            ApiV1IncidentsPartialUpdateManagedByContentTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_managed_by_object_id_error_component import (
            ApiV1IncidentsPartialUpdateManagedByObjectIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_modified_by_user_error_component import (
            ApiV1IncidentsPartialUpdateModifiedByUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_name_error_component import (
            ApiV1IncidentsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_non_field_errors_error_component import (
            ApiV1IncidentsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_notification_closed_sent_error_component import (
            ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_notification_opened_sent_error_component import (
            ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_occurred_at_error_component import (
            ApiV1IncidentsPartialUpdateOccurredAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_organization_id_error_component import (
            ApiV1IncidentsPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_platform_dns_record_created_error_component import (
            ApiV1IncidentsPartialUpdatePlatformDnsRecordCreatedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_platform_service_error_component import (
            ApiV1IncidentsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_provider_entity_error_component import (
            ApiV1IncidentsPartialUpdateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_provider_error_component import (
            ApiV1IncidentsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_provider_id_error_component import (
            ApiV1IncidentsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_provider_reference_error_component import (
            ApiV1IncidentsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_reconciliation_enabled_error_component import (
            ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_reference_url_error_component import (
            ApiV1IncidentsPartialUpdateReferenceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_reporter_error_component import (
            ApiV1IncidentsPartialUpdateReporterErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_resolved_at_error_component import (
            ApiV1IncidentsPartialUpdateResolvedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_scope_error_component import (
            ApiV1IncidentsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_sla_availability_error_component import (
            ApiV1IncidentsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_sla_target_error_component import (
            ApiV1IncidentsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_sla_window_days_error_component import (
            ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_slo_availability_error_component import (
            ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_slo_target_error_component import (
            ApiV1IncidentsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_slo_window_days_error_component import (
            ApiV1IncidentsPartialUpdateSloWindowDaysErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_source_datasource_error_component import (
            ApiV1IncidentsPartialUpdateSourceDatasourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_source_item_id_error_component import (
            ApiV1IncidentsPartialUpdateSourceItemIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_status_error_component import (
            ApiV1IncidentsPartialUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_target_availability_error_component import (
            ApiV1IncidentsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_vulnerability_finding_ids_error_component import (
            ApiV1IncidentsPartialUpdateVulnerabilityFindingIdsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_incidents_partial_update_workspace_id_error_component import (
            ApiV1IncidentsPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponent
                | ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponent
                | ApiV1IncidentsPartialUpdateAffectedVolumeIdsErrorComponent
                | ApiV1IncidentsPartialUpdateAnnotationsErrorComponent
                | ApiV1IncidentsPartialUpdateArchivedAtErrorComponent
                | ApiV1IncidentsPartialUpdateArchivedByErrorComponent
                | ApiV1IncidentsPartialUpdateArchivedErrorComponent
                | ApiV1IncidentsPartialUpdateArchivedReasonErrorComponent
                | ApiV1IncidentsPartialUpdateCreatedByComponentErrorComponent
                | ApiV1IncidentsPartialUpdateCreatedByUserErrorComponent
                | ApiV1IncidentsPartialUpdateCriticalityErrorComponent
                | ApiV1IncidentsPartialUpdateDebugModeErrorComponent
                | ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponent
                | ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1IncidentsPartialUpdateDisplayNameErrorComponent
                | ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponent
                | ApiV1IncidentsPartialUpdateKindErrorComponent
                | ApiV1IncidentsPartialUpdateLabelsErrorComponent
                | ApiV1IncidentsPartialUpdateLastReconciliationDurationSecondsErrorComponent
                | ApiV1IncidentsPartialUpdateManagedByContentTypeErrorComponent
                | ApiV1IncidentsPartialUpdateManagedByObjectIdErrorComponent
                | ApiV1IncidentsPartialUpdateModifiedByUserErrorComponent
                | ApiV1IncidentsPartialUpdateNameErrorComponent
                | ApiV1IncidentsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponent
                | ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponent
                | ApiV1IncidentsPartialUpdateOccurredAtErrorComponent
                | ApiV1IncidentsPartialUpdateOrganizationIdErrorComponent
                | ApiV1IncidentsPartialUpdatePlatformDnsRecordCreatedErrorComponent
                | ApiV1IncidentsPartialUpdatePlatformServiceErrorComponent
                | ApiV1IncidentsPartialUpdateProviderEntityErrorComponent
                | ApiV1IncidentsPartialUpdateProviderErrorComponent
                | ApiV1IncidentsPartialUpdateProviderIdErrorComponent
                | ApiV1IncidentsPartialUpdateProviderReferenceErrorComponent
                | ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1IncidentsPartialUpdateReferenceUrlErrorComponent
                | ApiV1IncidentsPartialUpdateReporterErrorComponent
                | ApiV1IncidentsPartialUpdateResolvedAtErrorComponent
                | ApiV1IncidentsPartialUpdateScopeErrorComponent
                | ApiV1IncidentsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1IncidentsPartialUpdateSlaTargetErrorComponent
                | ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponent
                | ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1IncidentsPartialUpdateSloTargetErrorComponent
                | ApiV1IncidentsPartialUpdateSloWindowDaysErrorComponent
                | ApiV1IncidentsPartialUpdateSourceDatasourceErrorComponent
                | ApiV1IncidentsPartialUpdateSourceItemIdErrorComponent
                | ApiV1IncidentsPartialUpdateStatusErrorComponent
                | ApiV1IncidentsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1IncidentsPartialUpdateVulnerabilityFindingIdsErrorComponent
                | ApiV1IncidentsPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_0 = (
                        ApiV1IncidentsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_1 = (
                        ApiV1IncidentsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_2 = (
                        ApiV1IncidentsPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_3 = (
                        ApiV1IncidentsPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_4 = (
                        ApiV1IncidentsPartialUpdateDowntimeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_5 = (
                        ApiV1IncidentsPartialUpdateAffectedHostIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_6 = (
                        ApiV1IncidentsPartialUpdateAffectedVolumeIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_7 = (
                        ApiV1IncidentsPartialUpdateAffectedPopIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_8 = (
                        ApiV1IncidentsPartialUpdateVulnerabilityFindingIdsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_9 = (
                        ApiV1IncidentsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_10 = (
                        ApiV1IncidentsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_11 = (
                        ApiV1IncidentsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_12 = (
                        ApiV1IncidentsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_13 = (
                        ApiV1IncidentsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_14 = (
                        ApiV1IncidentsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_15 = (
                        ApiV1IncidentsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_16 = (
                        ApiV1IncidentsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_17 = (
                        ApiV1IncidentsPartialUpdateLastReconciliationDurationSecondsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_18 = (
                        ApiV1IncidentsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_19 = (
                        ApiV1IncidentsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_20 = (
                        ApiV1IncidentsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_21 = (
                        ApiV1IncidentsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_22 = (
                        ApiV1IncidentsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_23 = (
                        ApiV1IncidentsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_24 = (
                        ApiV1IncidentsPartialUpdateCreatedByComponentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_25 = (
                        ApiV1IncidentsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_26 = (
                        ApiV1IncidentsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_27 = (
                        ApiV1IncidentsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_28 = (
                        ApiV1IncidentsPartialUpdateSloWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_29 = (
                        ApiV1IncidentsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_30 = (
                        ApiV1IncidentsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_31 = (
                        ApiV1IncidentsPartialUpdateSlaWindowDaysErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_32 = (
                        ApiV1IncidentsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_33 = (
                        ApiV1IncidentsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_34 = (
                        ApiV1IncidentsPartialUpdateManagedByObjectIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_35 = (
                        ApiV1IncidentsPartialUpdatePlatformDnsRecordCreatedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_36 = (
                        ApiV1IncidentsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_37 = (
                        ApiV1IncidentsPartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_38 = (
                        ApiV1IncidentsPartialUpdateOccurredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_39 = (
                        ApiV1IncidentsPartialUpdateDiscoveredAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_40 = (
                        ApiV1IncidentsPartialUpdateResolvedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_41 = (
                        ApiV1IncidentsPartialUpdateReporterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_42 = (
                        ApiV1IncidentsPartialUpdateReferenceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_43 = (
                        ApiV1IncidentsPartialUpdateSourceItemIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_44 = (
                        ApiV1IncidentsPartialUpdateNotificationOpenedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_45 = (
                        ApiV1IncidentsPartialUpdateNotificationClosedSentErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_46 = (
                        ApiV1IncidentsPartialUpdateArchivedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_46
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_47 = (
                        ApiV1IncidentsPartialUpdateManagedByContentTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_47
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_48 = (
                        ApiV1IncidentsPartialUpdateModifiedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_48
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_49 = (
                        ApiV1IncidentsPartialUpdateCreatedByUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_49
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_incidents_partial_update_error_type_50 = (
                        ApiV1IncidentsPartialUpdateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_incidents_partial_update_error_type_50
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_incidents_partial_update_error_type_51 = (
                    ApiV1IncidentsPartialUpdateSourceDatasourceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_incidents_partial_update_error_type_51

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_incidents_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_incidents_partial_update_validation_error.additional_properties = d
        return api_v1_incidents_partial_update_validation_error

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
