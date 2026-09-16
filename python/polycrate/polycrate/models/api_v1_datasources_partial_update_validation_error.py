from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_datasources_partial_update_annotations_error_component import (
        ApiV1DatasourcesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_archived_at_error_component import (
        ApiV1DatasourcesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_archived_error_component import (
        ApiV1DatasourcesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_archived_reason_error_component import (
        ApiV1DatasourcesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_create_incidents_error_component import (
        ApiV1DatasourcesPartialUpdateCreateIncidentsErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_create_incidents_without_resources_error_component import (
        ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_create_maintenance_as_draft_error_component import (
        ApiV1DatasourcesPartialUpdateCreateMaintenanceAsDraftErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_create_notes_resolved_error_component import (
        ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_criticality_error_component import (
        ApiV1DatasourcesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_datasource_url_error_component import (
        ApiV1DatasourcesPartialUpdateDatasourceUrlErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_debug_mode_error_component import (
        ApiV1DatasourcesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_display_name_error_component import (
        ApiV1DatasourcesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_is_enabled_error_component import (
        ApiV1DatasourcesPartialUpdateIsEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_kind_error_component import (
        ApiV1DatasourcesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_labels_error_component import (
        ApiV1DatasourcesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_last_sync_error_component import (
        ApiV1DatasourcesPartialUpdateLastSyncErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_last_sync_error_error_component import (
        ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_name_error_component import (
        ApiV1DatasourcesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_non_field_errors_error_component import (
        ApiV1DatasourcesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_note_kind_error_component import (
        ApiV1DatasourcesPartialUpdateNoteKindErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_note_organization_id_error_component import (
        ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_note_workspace_id_error_component import (
        ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_platform_service_error_component import (
        ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_provider_entity_id_error_component import (
        ApiV1DatasourcesPartialUpdateProviderEntityIdErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_provider_error_component import (
        ApiV1DatasourcesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_provider_id_error_component import (
        ApiV1DatasourcesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_provider_reference_error_component import (
        ApiV1DatasourcesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_reconciliation_enabled_error_component import (
        ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_sla_availability_error_component import (
        ApiV1DatasourcesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_sla_target_error_component import (
        ApiV1DatasourcesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_slo_availability_error_component import (
        ApiV1DatasourcesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_slo_target_error_component import (
        ApiV1DatasourcesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_sync_interval_minutes_error_component import (
        ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_target_availability_error_component import (
        ApiV1DatasourcesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_datasources_partial_update_tolerations_error_component import (
        ApiV1DatasourcesPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1DatasourcesPartialUpdateValidationError")


@_attrs_define
class ApiV1DatasourcesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1DatasourcesPartialUpdateAnnotationsErrorComponent |
            ApiV1DatasourcesPartialUpdateArchivedAtErrorComponent | ApiV1DatasourcesPartialUpdateArchivedErrorComponent |
            ApiV1DatasourcesPartialUpdateArchivedReasonErrorComponent |
            ApiV1DatasourcesPartialUpdateCreateIncidentsErrorComponent |
            ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponent |
            ApiV1DatasourcesPartialUpdateCreateMaintenanceAsDraftErrorComponent |
            ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponent |
            ApiV1DatasourcesPartialUpdateCriticalityErrorComponent |
            ApiV1DatasourcesPartialUpdateDatasourceUrlErrorComponent | ApiV1DatasourcesPartialUpdateDebugModeErrorComponent
            | ApiV1DatasourcesPartialUpdateDisplayNameErrorComponent | ApiV1DatasourcesPartialUpdateIsEnabledErrorComponent
            | ApiV1DatasourcesPartialUpdateKindErrorComponent | ApiV1DatasourcesPartialUpdateLabelsErrorComponent |
            ApiV1DatasourcesPartialUpdateLastSyncErrorComponent | ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponent |
            ApiV1DatasourcesPartialUpdateNameErrorComponent | ApiV1DatasourcesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1DatasourcesPartialUpdateNoteKindErrorComponent |
            ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponent |
            ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponent |
            ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponent |
            ApiV1DatasourcesPartialUpdateProviderEntityIdErrorComponent |
            ApiV1DatasourcesPartialUpdateProviderErrorComponent | ApiV1DatasourcesPartialUpdateProviderIdErrorComponent |
            ApiV1DatasourcesPartialUpdateProviderReferenceErrorComponent |
            ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1DatasourcesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1DatasourcesPartialUpdateSlaTargetErrorComponent |
            ApiV1DatasourcesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1DatasourcesPartialUpdateSloTargetErrorComponent |
            ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponent |
            ApiV1DatasourcesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1DatasourcesPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1DatasourcesPartialUpdateAnnotationsErrorComponent
        | ApiV1DatasourcesPartialUpdateArchivedAtErrorComponent
        | ApiV1DatasourcesPartialUpdateArchivedErrorComponent
        | ApiV1DatasourcesPartialUpdateArchivedReasonErrorComponent
        | ApiV1DatasourcesPartialUpdateCreateIncidentsErrorComponent
        | ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponent
        | ApiV1DatasourcesPartialUpdateCreateMaintenanceAsDraftErrorComponent
        | ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponent
        | ApiV1DatasourcesPartialUpdateCriticalityErrorComponent
        | ApiV1DatasourcesPartialUpdateDatasourceUrlErrorComponent
        | ApiV1DatasourcesPartialUpdateDebugModeErrorComponent
        | ApiV1DatasourcesPartialUpdateDisplayNameErrorComponent
        | ApiV1DatasourcesPartialUpdateIsEnabledErrorComponent
        | ApiV1DatasourcesPartialUpdateKindErrorComponent
        | ApiV1DatasourcesPartialUpdateLabelsErrorComponent
        | ApiV1DatasourcesPartialUpdateLastSyncErrorComponent
        | ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponent
        | ApiV1DatasourcesPartialUpdateNameErrorComponent
        | ApiV1DatasourcesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1DatasourcesPartialUpdateNoteKindErrorComponent
        | ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponent
        | ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponent
        | ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponent
        | ApiV1DatasourcesPartialUpdateProviderEntityIdErrorComponent
        | ApiV1DatasourcesPartialUpdateProviderErrorComponent
        | ApiV1DatasourcesPartialUpdateProviderIdErrorComponent
        | ApiV1DatasourcesPartialUpdateProviderReferenceErrorComponent
        | ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1DatasourcesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1DatasourcesPartialUpdateSlaTargetErrorComponent
        | ApiV1DatasourcesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1DatasourcesPartialUpdateSloTargetErrorComponent
        | ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponent
        | ApiV1DatasourcesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1DatasourcesPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_datasources_partial_update_annotations_error_component import (
            ApiV1DatasourcesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_archived_at_error_component import (
            ApiV1DatasourcesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_archived_error_component import (
            ApiV1DatasourcesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_archived_reason_error_component import (
            ApiV1DatasourcesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_create_incidents_error_component import (
            ApiV1DatasourcesPartialUpdateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesPartialUpdateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_create_notes_resolved_error_component import (
            ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_criticality_error_component import (
            ApiV1DatasourcesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_datasource_url_error_component import (
            ApiV1DatasourcesPartialUpdateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_debug_mode_error_component import (
            ApiV1DatasourcesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_display_name_error_component import (
            ApiV1DatasourcesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_is_enabled_error_component import (
            ApiV1DatasourcesPartialUpdateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_kind_error_component import (
            ApiV1DatasourcesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_labels_error_component import (
            ApiV1DatasourcesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_last_sync_error_component import (
            ApiV1DatasourcesPartialUpdateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_last_sync_error_error_component import (
            ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_name_error_component import (
            ApiV1DatasourcesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_non_field_errors_error_component import (
            ApiV1DatasourcesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_note_kind_error_component import (
            ApiV1DatasourcesPartialUpdateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_note_organization_id_error_component import (
            ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_note_workspace_id_error_component import (
            ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_platform_service_error_component import (
            ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_provider_error_component import (
            ApiV1DatasourcesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_provider_id_error_component import (
            ApiV1DatasourcesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_provider_reference_error_component import (
            ApiV1DatasourcesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_reconciliation_enabled_error_component import (
            ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_sla_availability_error_component import (
            ApiV1DatasourcesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_sla_target_error_component import (
            ApiV1DatasourcesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_slo_availability_error_component import (
            ApiV1DatasourcesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_slo_target_error_component import (
            ApiV1DatasourcesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_sync_interval_minutes_error_component import (
            ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_target_availability_error_component import (
            ApiV1DatasourcesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_tolerations_error_component import (
            ApiV1DatasourcesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateDatasourceUrlErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateIsEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateNoteKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateCreateMaintenanceAsDraftErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateCreateIncidentsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateLastSyncErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponent):
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
        from ..models.api_v1_datasources_partial_update_annotations_error_component import (
            ApiV1DatasourcesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_archived_at_error_component import (
            ApiV1DatasourcesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_archived_error_component import (
            ApiV1DatasourcesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_archived_reason_error_component import (
            ApiV1DatasourcesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_create_incidents_error_component import (
            ApiV1DatasourcesPartialUpdateCreateIncidentsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_create_incidents_without_resources_error_component import (
            ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_create_maintenance_as_draft_error_component import (
            ApiV1DatasourcesPartialUpdateCreateMaintenanceAsDraftErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_create_notes_resolved_error_component import (
            ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_criticality_error_component import (
            ApiV1DatasourcesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_datasource_url_error_component import (
            ApiV1DatasourcesPartialUpdateDatasourceUrlErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_debug_mode_error_component import (
            ApiV1DatasourcesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_display_name_error_component import (
            ApiV1DatasourcesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_is_enabled_error_component import (
            ApiV1DatasourcesPartialUpdateIsEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_kind_error_component import (
            ApiV1DatasourcesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_labels_error_component import (
            ApiV1DatasourcesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_last_sync_error_component import (
            ApiV1DatasourcesPartialUpdateLastSyncErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_last_sync_error_error_component import (
            ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_name_error_component import (
            ApiV1DatasourcesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_non_field_errors_error_component import (
            ApiV1DatasourcesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_note_kind_error_component import (
            ApiV1DatasourcesPartialUpdateNoteKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_note_organization_id_error_component import (
            ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_note_workspace_id_error_component import (
            ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_platform_service_error_component import (
            ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_provider_entity_id_error_component import (
            ApiV1DatasourcesPartialUpdateProviderEntityIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_provider_error_component import (
            ApiV1DatasourcesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_provider_id_error_component import (
            ApiV1DatasourcesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_provider_reference_error_component import (
            ApiV1DatasourcesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_reconciliation_enabled_error_component import (
            ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_sla_availability_error_component import (
            ApiV1DatasourcesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_sla_target_error_component import (
            ApiV1DatasourcesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_slo_availability_error_component import (
            ApiV1DatasourcesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_slo_target_error_component import (
            ApiV1DatasourcesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_sync_interval_minutes_error_component import (
            ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_target_availability_error_component import (
            ApiV1DatasourcesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_datasources_partial_update_tolerations_error_component import (
            ApiV1DatasourcesPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1DatasourcesPartialUpdateAnnotationsErrorComponent
                | ApiV1DatasourcesPartialUpdateArchivedAtErrorComponent
                | ApiV1DatasourcesPartialUpdateArchivedErrorComponent
                | ApiV1DatasourcesPartialUpdateArchivedReasonErrorComponent
                | ApiV1DatasourcesPartialUpdateCreateIncidentsErrorComponent
                | ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponent
                | ApiV1DatasourcesPartialUpdateCreateMaintenanceAsDraftErrorComponent
                | ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponent
                | ApiV1DatasourcesPartialUpdateCriticalityErrorComponent
                | ApiV1DatasourcesPartialUpdateDatasourceUrlErrorComponent
                | ApiV1DatasourcesPartialUpdateDebugModeErrorComponent
                | ApiV1DatasourcesPartialUpdateDisplayNameErrorComponent
                | ApiV1DatasourcesPartialUpdateIsEnabledErrorComponent
                | ApiV1DatasourcesPartialUpdateKindErrorComponent
                | ApiV1DatasourcesPartialUpdateLabelsErrorComponent
                | ApiV1DatasourcesPartialUpdateLastSyncErrorComponent
                | ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponent
                | ApiV1DatasourcesPartialUpdateNameErrorComponent
                | ApiV1DatasourcesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1DatasourcesPartialUpdateNoteKindErrorComponent
                | ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponent
                | ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponent
                | ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponent
                | ApiV1DatasourcesPartialUpdateProviderEntityIdErrorComponent
                | ApiV1DatasourcesPartialUpdateProviderErrorComponent
                | ApiV1DatasourcesPartialUpdateProviderIdErrorComponent
                | ApiV1DatasourcesPartialUpdateProviderReferenceErrorComponent
                | ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1DatasourcesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1DatasourcesPartialUpdateSlaTargetErrorComponent
                | ApiV1DatasourcesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1DatasourcesPartialUpdateSloTargetErrorComponent
                | ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponent
                | ApiV1DatasourcesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1DatasourcesPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_0 = (
                        ApiV1DatasourcesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_1 = (
                        ApiV1DatasourcesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_2 = (
                        ApiV1DatasourcesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_3 = (
                        ApiV1DatasourcesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_4 = (
                        ApiV1DatasourcesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_5 = (
                        ApiV1DatasourcesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_6 = (
                        ApiV1DatasourcesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_7 = (
                        ApiV1DatasourcesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_8 = (
                        ApiV1DatasourcesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_9 = (
                        ApiV1DatasourcesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_10 = (
                        ApiV1DatasourcesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_11 = (
                        ApiV1DatasourcesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_12 = (
                        ApiV1DatasourcesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_13 = (
                        ApiV1DatasourcesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_14 = (
                        ApiV1DatasourcesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_15 = (
                        ApiV1DatasourcesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_16 = (
                        ApiV1DatasourcesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_17 = (
                        ApiV1DatasourcesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_18 = (
                        ApiV1DatasourcesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_19 = (
                        ApiV1DatasourcesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_20 = (
                        ApiV1DatasourcesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_21 = (
                        ApiV1DatasourcesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_22 = (
                        ApiV1DatasourcesPartialUpdateDatasourceUrlErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_23 = (
                        ApiV1DatasourcesPartialUpdateIsEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_24 = (
                        ApiV1DatasourcesPartialUpdateSyncIntervalMinutesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_25 = (
                        ApiV1DatasourcesPartialUpdateNoteKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_26 = (
                        ApiV1DatasourcesPartialUpdateNoteOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_27 = (
                        ApiV1DatasourcesPartialUpdateNoteWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_28 = (
                        ApiV1DatasourcesPartialUpdateCreateNotesResolvedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_29 = (
                        ApiV1DatasourcesPartialUpdateCreateMaintenanceAsDraftErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_30 = (
                        ApiV1DatasourcesPartialUpdateCreateIncidentsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_31 = (
                        ApiV1DatasourcesPartialUpdateCreateIncidentsWithoutResourcesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_32 = (
                        ApiV1DatasourcesPartialUpdateLastSyncErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_datasources_partial_update_error_type_33 = (
                        ApiV1DatasourcesPartialUpdateLastSyncErrorErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_datasources_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_datasources_partial_update_error_type_34 = (
                    ApiV1DatasourcesPartialUpdateProviderEntityIdErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_datasources_partial_update_error_type_34

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_datasources_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_datasources_partial_update_validation_error.additional_properties = d
        return api_v1_datasources_partial_update_validation_error

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
