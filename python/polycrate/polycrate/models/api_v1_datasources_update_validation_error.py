from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_datasources_update_annotations_error_component import (
        ApiV1DatasourcesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_datasources_update_archived_at_error_component import (
        ApiV1DatasourcesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_datasources_update_archived_error_component import ApiV1DatasourcesUpdateArchivedErrorComponent
    from ..models.api_v1_datasources_update_archived_reason_error_component import (
        ApiV1DatasourcesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_datasources_update_create_incidents_error_component import (
        ApiV1DatasourcesUpdateCreateIncidentsErrorComponent,
    )
    from ..models.api_v1_datasources_update_create_incidents_without_resources_error_component import (
        ApiV1DatasourcesUpdateCreateIncidentsWithoutResourcesErrorComponent,
    )
    from ..models.api_v1_datasources_update_create_maintenance_as_draft_error_component import (
        ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponent,
    )
    from ..models.api_v1_datasources_update_create_notes_resolved_error_component import (
        ApiV1DatasourcesUpdateCreateNotesResolvedErrorComponent,
    )
    from ..models.api_v1_datasources_update_criticality_error_component import (
        ApiV1DatasourcesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_datasources_update_datasource_url_error_component import (
        ApiV1DatasourcesUpdateDatasourceUrlErrorComponent,
    )
    from ..models.api_v1_datasources_update_debug_mode_error_component import (
        ApiV1DatasourcesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_datasources_update_display_name_error_component import (
        ApiV1DatasourcesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_datasources_update_is_enabled_error_component import (
        ApiV1DatasourcesUpdateIsEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_update_kind_error_component import ApiV1DatasourcesUpdateKindErrorComponent
    from ..models.api_v1_datasources_update_labels_error_component import ApiV1DatasourcesUpdateLabelsErrorComponent
    from ..models.api_v1_datasources_update_last_sync_error_component import (
        ApiV1DatasourcesUpdateLastSyncErrorComponent,
    )
    from ..models.api_v1_datasources_update_last_sync_error_error_component import (
        ApiV1DatasourcesUpdateLastSyncErrorErrorComponent,
    )
    from ..models.api_v1_datasources_update_name_error_component import ApiV1DatasourcesUpdateNameErrorComponent
    from ..models.api_v1_datasources_update_non_field_errors_error_component import (
        ApiV1DatasourcesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_datasources_update_note_kind_error_component import (
        ApiV1DatasourcesUpdateNoteKindErrorComponent,
    )
    from ..models.api_v1_datasources_update_note_organization_id_error_component import (
        ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponent,
    )
    from ..models.api_v1_datasources_update_note_workspace_id_error_component import (
        ApiV1DatasourcesUpdateNoteWorkspaceIdErrorComponent,
    )
    from ..models.api_v1_datasources_update_platform_service_error_component import (
        ApiV1DatasourcesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_datasources_update_provider_entity_id_error_component import (
        ApiV1DatasourcesUpdateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_datasources_update_provider_error_component import ApiV1DatasourcesUpdateProviderErrorComponent
    from ..models.api_v1_datasources_update_provider_id_error_component import (
        ApiV1DatasourcesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_datasources_update_provider_reference_error_component import (
        ApiV1DatasourcesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_datasources_update_reconciliation_enabled_error_component import (
        ApiV1DatasourcesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_update_sla_availability_error_component import (
        ApiV1DatasourcesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_update_sla_target_error_component import (
        ApiV1DatasourcesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_datasources_update_slo_availability_error_component import (
        ApiV1DatasourcesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_update_slo_target_error_component import (
        ApiV1DatasourcesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_datasources_update_sync_interval_minutes_error_component import (
        ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponent,
    )
    from ..models.api_v1_datasources_update_target_availability_error_component import (
        ApiV1DatasourcesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_update_tolerations_error_component import (
        ApiV1DatasourcesUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DatasourcesUpdateValidationError")


@_attrs_define
class ApiV1DatasourcesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DatasourcesUpdateAnnotationsErrorComponent | ApiV1DatasourcesUpdateArchivedAtErrorComponent |
            ApiV1DatasourcesUpdateArchivedErrorComponent | ApiV1DatasourcesUpdateArchivedReasonErrorComponent |
            ApiV1DatasourcesUpdateCreateIncidentsErrorComponent |
            ApiV1DatasourcesUpdateCreateIncidentsWithoutResourcesErrorComponent |
            ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponent |
            ApiV1DatasourcesUpdateCreateNotesResolvedErrorComponent | ApiV1DatasourcesUpdateCriticalityErrorComponent |
            ApiV1DatasourcesUpdateDatasourceUrlErrorComponent | ApiV1DatasourcesUpdateDebugModeErrorComponent |
            ApiV1DatasourcesUpdateDisplayNameErrorComponent | ApiV1DatasourcesUpdateIsEnabledErrorComponent |
            ApiV1DatasourcesUpdateKindErrorComponent | ApiV1DatasourcesUpdateLabelsErrorComponent |
            ApiV1DatasourcesUpdateLastSyncErrorComponent | ApiV1DatasourcesUpdateLastSyncErrorErrorComponent |
            ApiV1DatasourcesUpdateNameErrorComponent | ApiV1DatasourcesUpdateNonFieldErrorsErrorComponent |
            ApiV1DatasourcesUpdateNoteKindErrorComponent | ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponent |
            ApiV1DatasourcesUpdateNoteWorkspaceIdErrorComponent | ApiV1DatasourcesUpdatePlatformServiceErrorComponent |
            ApiV1DatasourcesUpdateProviderEntityIdErrorComponent | ApiV1DatasourcesUpdateProviderErrorComponent |
            ApiV1DatasourcesUpdateProviderIdErrorComponent | ApiV1DatasourcesUpdateProviderReferenceErrorComponent |
            ApiV1DatasourcesUpdateReconciliationEnabledErrorComponent | ApiV1DatasourcesUpdateSlaAvailabilityErrorComponent
            | ApiV1DatasourcesUpdateSlaTargetErrorComponent | ApiV1DatasourcesUpdateSloAvailabilityErrorComponent |
            ApiV1DatasourcesUpdateSloTargetErrorComponent | ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponent |
            ApiV1DatasourcesUpdateTargetAvailabilityErrorComponent | ApiV1DatasourcesUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DatasourcesUpdateAnnotationsErrorComponent
        | ApiV1DatasourcesUpdateArchivedAtErrorComponent
        | ApiV1DatasourcesUpdateArchivedErrorComponent
        | ApiV1DatasourcesUpdateArchivedReasonErrorComponent
        | ApiV1DatasourcesUpdateCreateIncidentsErrorComponent
        | ApiV1DatasourcesUpdateCreateIncidentsWithoutResourcesErrorComponent
        | ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponent
        | ApiV1DatasourcesUpdateCreateNotesResolvedErrorComponent
        | ApiV1DatasourcesUpdateCriticalityErrorComponent
        | ApiV1DatasourcesUpdateDatasourceUrlErrorComponent
        | ApiV1DatasourcesUpdateDebugModeErrorComponent
        | ApiV1DatasourcesUpdateDisplayNameErrorComponent
        | ApiV1DatasourcesUpdateIsEnabledErrorComponent
        | ApiV1DatasourcesUpdateKindErrorComponent
        | ApiV1DatasourcesUpdateLabelsErrorComponent
        | ApiV1DatasourcesUpdateLastSyncErrorComponent
        | ApiV1DatasourcesUpdateLastSyncErrorErrorComponent
        | ApiV1DatasourcesUpdateNameErrorComponent
        | ApiV1DatasourcesUpdateNonFieldErrorsErrorComponent
        | ApiV1DatasourcesUpdateNoteKindErrorComponent
        | ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponent
        | ApiV1DatasourcesUpdateNoteWorkspaceIdErrorComponent
        | ApiV1DatasourcesUpdatePlatformServiceErrorComponent
        | ApiV1DatasourcesUpdateProviderEntityIdErrorComponent
        | ApiV1DatasourcesUpdateProviderErrorComponent
        | ApiV1DatasourcesUpdateProviderIdErrorComponent
        | ApiV1DatasourcesUpdateProviderReferenceErrorComponent
        | ApiV1DatasourcesUpdateReconciliationEnabledErrorComponent
        | ApiV1DatasourcesUpdateSlaAvailabilityErrorComponent
        | ApiV1DatasourcesUpdateSlaTargetErrorComponent
        | ApiV1DatasourcesUpdateSloAvailabilityErrorComponent
        | ApiV1DatasourcesUpdateSloTargetErrorComponent
        | ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponent
        | ApiV1DatasourcesUpdateTargetAvailabilityErrorComponent
        | ApiV1DatasourcesUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_datasources_update_annotations_error_component import (
            ApiV1DatasourcesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_datasources_update_archived_at_error_component import (
            ApiV1DatasourcesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_datasources_update_archived_error_component import (
            ApiV1DatasourcesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_datasources_update_archived_reason_error_component import (
            ApiV1DatasourcesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_datasources_update_create_incidents_error_component import (
            ApiV1DatasourcesUpdateCreateIncidentsErrorComponent,
        )
        from ..models.api_v1_datasources_update_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesUpdateCreateIncidentsWithoutResourcesErrorComponent,
        )
        from ..models.api_v1_datasources_update_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponent,
        )
        from ..models.api_v1_datasources_update_create_notes_resolved_error_component import (
            ApiV1DatasourcesUpdateCreateNotesResolvedErrorComponent,
        )
        from ..models.api_v1_datasources_update_criticality_error_component import (
            ApiV1DatasourcesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_datasources_update_datasource_url_error_component import (
            ApiV1DatasourcesUpdateDatasourceUrlErrorComponent,
        )
        from ..models.api_v1_datasources_update_debug_mode_error_component import (
            ApiV1DatasourcesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_datasources_update_display_name_error_component import (
            ApiV1DatasourcesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_datasources_update_is_enabled_error_component import (
            ApiV1DatasourcesUpdateIsEnabledErrorComponent,
        )
        from ..models.api_v1_datasources_update_kind_error_component import ApiV1DatasourcesUpdateKindErrorComponent
        from ..models.api_v1_datasources_update_labels_error_component import ApiV1DatasourcesUpdateLabelsErrorComponent
        from ..models.api_v1_datasources_update_last_sync_error_component import (
            ApiV1DatasourcesUpdateLastSyncErrorComponent,
        )
        from ..models.api_v1_datasources_update_last_sync_error_error_component import (
            ApiV1DatasourcesUpdateLastSyncErrorErrorComponent,
        )
        from ..models.api_v1_datasources_update_name_error_component import ApiV1DatasourcesUpdateNameErrorComponent
        from ..models.api_v1_datasources_update_non_field_errors_error_component import (
            ApiV1DatasourcesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_datasources_update_note_kind_error_component import (
            ApiV1DatasourcesUpdateNoteKindErrorComponent,
        )
        from ..models.api_v1_datasources_update_note_organization_id_error_component import (
            ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponent,
        )
        from ..models.api_v1_datasources_update_note_workspace_id_error_component import (
            ApiV1DatasourcesUpdateNoteWorkspaceIdErrorComponent,
        )
        from ..models.api_v1_datasources_update_platform_service_error_component import (
            ApiV1DatasourcesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_datasources_update_provider_error_component import (
            ApiV1DatasourcesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_datasources_update_provider_id_error_component import (
            ApiV1DatasourcesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_datasources_update_provider_reference_error_component import (
            ApiV1DatasourcesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_datasources_update_reconciliation_enabled_error_component import (
            ApiV1DatasourcesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_datasources_update_sla_availability_error_component import (
            ApiV1DatasourcesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_datasources_update_sla_target_error_component import (
            ApiV1DatasourcesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_datasources_update_slo_availability_error_component import (
            ApiV1DatasourcesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_datasources_update_slo_target_error_component import (
            ApiV1DatasourcesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_datasources_update_sync_interval_minutes_error_component import (
            ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponent,
        )
        from ..models.api_v1_datasources_update_target_availability_error_component import (
            ApiV1DatasourcesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_datasources_update_tolerations_error_component import (
            ApiV1DatasourcesUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DatasourcesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateDatasourceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateNoteKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateNoteWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateCreateNotesResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateCreateIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateCreateIncidentsWithoutResourcesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateLastSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesUpdateLastSyncErrorErrorComponent):
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
        from ..models.api_v1_datasources_update_annotations_error_component import (
            ApiV1DatasourcesUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_datasources_update_archived_at_error_component import (
            ApiV1DatasourcesUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_datasources_update_archived_error_component import (
            ApiV1DatasourcesUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_datasources_update_archived_reason_error_component import (
            ApiV1DatasourcesUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_datasources_update_create_incidents_error_component import (
            ApiV1DatasourcesUpdateCreateIncidentsErrorComponent,
        )
        from ..models.api_v1_datasources_update_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesUpdateCreateIncidentsWithoutResourcesErrorComponent,
        )
        from ..models.api_v1_datasources_update_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponent,
        )
        from ..models.api_v1_datasources_update_create_notes_resolved_error_component import (
            ApiV1DatasourcesUpdateCreateNotesResolvedErrorComponent,
        )
        from ..models.api_v1_datasources_update_criticality_error_component import (
            ApiV1DatasourcesUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_datasources_update_datasource_url_error_component import (
            ApiV1DatasourcesUpdateDatasourceUrlErrorComponent,
        )
        from ..models.api_v1_datasources_update_debug_mode_error_component import (
            ApiV1DatasourcesUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_datasources_update_display_name_error_component import (
            ApiV1DatasourcesUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_datasources_update_is_enabled_error_component import (
            ApiV1DatasourcesUpdateIsEnabledErrorComponent,
        )
        from ..models.api_v1_datasources_update_kind_error_component import ApiV1DatasourcesUpdateKindErrorComponent
        from ..models.api_v1_datasources_update_labels_error_component import ApiV1DatasourcesUpdateLabelsErrorComponent
        from ..models.api_v1_datasources_update_last_sync_error_component import (
            ApiV1DatasourcesUpdateLastSyncErrorComponent,
        )
        from ..models.api_v1_datasources_update_last_sync_error_error_component import (
            ApiV1DatasourcesUpdateLastSyncErrorErrorComponent,
        )
        from ..models.api_v1_datasources_update_name_error_component import ApiV1DatasourcesUpdateNameErrorComponent
        from ..models.api_v1_datasources_update_non_field_errors_error_component import (
            ApiV1DatasourcesUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_datasources_update_note_kind_error_component import (
            ApiV1DatasourcesUpdateNoteKindErrorComponent,
        )
        from ..models.api_v1_datasources_update_note_organization_id_error_component import (
            ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponent,
        )
        from ..models.api_v1_datasources_update_note_workspace_id_error_component import (
            ApiV1DatasourcesUpdateNoteWorkspaceIdErrorComponent,
        )
        from ..models.api_v1_datasources_update_platform_service_error_component import (
            ApiV1DatasourcesUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_datasources_update_provider_entity_id_error_component import (
            ApiV1DatasourcesUpdateProviderEntityIdErrorComponent,
        )
        from ..models.api_v1_datasources_update_provider_error_component import (
            ApiV1DatasourcesUpdateProviderErrorComponent,
        )
        from ..models.api_v1_datasources_update_provider_id_error_component import (
            ApiV1DatasourcesUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_datasources_update_provider_reference_error_component import (
            ApiV1DatasourcesUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_datasources_update_reconciliation_enabled_error_component import (
            ApiV1DatasourcesUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_datasources_update_sla_availability_error_component import (
            ApiV1DatasourcesUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_datasources_update_sla_target_error_component import (
            ApiV1DatasourcesUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_datasources_update_slo_availability_error_component import (
            ApiV1DatasourcesUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_datasources_update_slo_target_error_component import (
            ApiV1DatasourcesUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_datasources_update_sync_interval_minutes_error_component import (
            ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponent,
        )
        from ..models.api_v1_datasources_update_target_availability_error_component import (
            ApiV1DatasourcesUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_datasources_update_tolerations_error_component import (
            ApiV1DatasourcesUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DatasourcesUpdateAnnotationsErrorComponent
                | ApiV1DatasourcesUpdateArchivedAtErrorComponent
                | ApiV1DatasourcesUpdateArchivedErrorComponent
                | ApiV1DatasourcesUpdateArchivedReasonErrorComponent
                | ApiV1DatasourcesUpdateCreateIncidentsErrorComponent
                | ApiV1DatasourcesUpdateCreateIncidentsWithoutResourcesErrorComponent
                | ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponent
                | ApiV1DatasourcesUpdateCreateNotesResolvedErrorComponent
                | ApiV1DatasourcesUpdateCriticalityErrorComponent
                | ApiV1DatasourcesUpdateDatasourceUrlErrorComponent
                | ApiV1DatasourcesUpdateDebugModeErrorComponent
                | ApiV1DatasourcesUpdateDisplayNameErrorComponent
                | ApiV1DatasourcesUpdateIsEnabledErrorComponent
                | ApiV1DatasourcesUpdateKindErrorComponent
                | ApiV1DatasourcesUpdateLabelsErrorComponent
                | ApiV1DatasourcesUpdateLastSyncErrorComponent
                | ApiV1DatasourcesUpdateLastSyncErrorErrorComponent
                | ApiV1DatasourcesUpdateNameErrorComponent
                | ApiV1DatasourcesUpdateNonFieldErrorsErrorComponent
                | ApiV1DatasourcesUpdateNoteKindErrorComponent
                | ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponent
                | ApiV1DatasourcesUpdateNoteWorkspaceIdErrorComponent
                | ApiV1DatasourcesUpdatePlatformServiceErrorComponent
                | ApiV1DatasourcesUpdateProviderEntityIdErrorComponent
                | ApiV1DatasourcesUpdateProviderErrorComponent
                | ApiV1DatasourcesUpdateProviderIdErrorComponent
                | ApiV1DatasourcesUpdateProviderReferenceErrorComponent
                | ApiV1DatasourcesUpdateReconciliationEnabledErrorComponent
                | ApiV1DatasourcesUpdateSlaAvailabilityErrorComponent
                | ApiV1DatasourcesUpdateSlaTargetErrorComponent
                | ApiV1DatasourcesUpdateSloAvailabilityErrorComponent
                | ApiV1DatasourcesUpdateSloTargetErrorComponent
                | ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponent
                | ApiV1DatasourcesUpdateTargetAvailabilityErrorComponent
                | ApiV1DatasourcesUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_0 = (
                        ApiV1DatasourcesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_1 = (
                        ApiV1DatasourcesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_2 = (
                        ApiV1DatasourcesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_3 = (
                        ApiV1DatasourcesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_4 = (
                        ApiV1DatasourcesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_5 = (
                        ApiV1DatasourcesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_6 = (
                        ApiV1DatasourcesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_7 = (
                        ApiV1DatasourcesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_8 = (
                        ApiV1DatasourcesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_9 = (
                        ApiV1DatasourcesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_10 = (
                        ApiV1DatasourcesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_11 = (
                        ApiV1DatasourcesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_12 = (
                        ApiV1DatasourcesUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_13 = (
                        ApiV1DatasourcesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_14 = (
                        ApiV1DatasourcesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_15 = (
                        ApiV1DatasourcesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_16 = (
                        ApiV1DatasourcesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_17 = (
                        ApiV1DatasourcesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_18 = (
                        ApiV1DatasourcesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_19 = (
                        ApiV1DatasourcesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_20 = (
                        ApiV1DatasourcesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_21 = (
                        ApiV1DatasourcesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_22 = (
                        ApiV1DatasourcesUpdateDatasourceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_23 = (
                        ApiV1DatasourcesUpdateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_24 = (
                        ApiV1DatasourcesUpdateSyncIntervalMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_25 = (
                        ApiV1DatasourcesUpdateNoteKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_26 = (
                        ApiV1DatasourcesUpdateNoteOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_27 = (
                        ApiV1DatasourcesUpdateNoteWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_28 = (
                        ApiV1DatasourcesUpdateCreateNotesResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_29 = (
                        ApiV1DatasourcesUpdateCreateMaintenanceAsDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_30 = (
                        ApiV1DatasourcesUpdateCreateIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_31 = (
                        ApiV1DatasourcesUpdateCreateIncidentsWithoutResourcesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_32 = (
                        ApiV1DatasourcesUpdateLastSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_update_error_type_33 = (
                        ApiV1DatasourcesUpdateLastSyncErrorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_datasources_update_error_type_34 = (
                    ApiV1DatasourcesUpdateProviderEntityIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_datasources_update_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_datasources_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_datasources_update_validation_error.additional_properties = d
        return api_v1_datasources_update_validation_error

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
