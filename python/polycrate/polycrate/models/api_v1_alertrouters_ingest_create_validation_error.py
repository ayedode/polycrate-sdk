from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertrouters_ingest_create_annotations_error_component import (
        ApiV1AlertroutersIngestCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_archived_at_error_component import (
        ApiV1AlertroutersIngestCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_archived_error_component import (
        ApiV1AlertroutersIngestCreateArchivedErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_archived_reason_error_component import (
        ApiV1AlertroutersIngestCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_criticality_error_component import (
        ApiV1AlertroutersIngestCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_debug_mode_error_component import (
        ApiV1AlertroutersIngestCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_display_name_error_component import (
        ApiV1AlertroutersIngestCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_kind_error_component import (
        ApiV1AlertroutersIngestCreateKindErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_label_cluster_error_component import (
        ApiV1AlertroutersIngestCreateLabelClusterErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_label_criticality_error_component import (
        ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_label_namespace_error_component import (
        ApiV1AlertroutersIngestCreateLabelNamespaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_label_organization_error_component import (
        ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_label_pod_error_component import (
        ApiV1AlertroutersIngestCreateLabelPodErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_label_workspace_error_component import (
        ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_labels_error_component import (
        ApiV1AlertroutersIngestCreateLabelsErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_name_error_component import (
        ApiV1AlertroutersIngestCreateNameErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_non_field_errors_error_component import (
        ApiV1AlertroutersIngestCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_organization_id_error_component import (
        ApiV1AlertroutersIngestCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_platform_service_error_component import (
        ApiV1AlertroutersIngestCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_provider_error_component import (
        ApiV1AlertroutersIngestCreateProviderErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_provider_id_error_component import (
        ApiV1AlertroutersIngestCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_provider_reference_error_component import (
        ApiV1AlertroutersIngestCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_reconciliation_enabled_error_component import (
        ApiV1AlertroutersIngestCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_sla_availability_error_component import (
        ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_sla_target_error_component import (
        ApiV1AlertroutersIngestCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_slo_availability_error_component import (
        ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_slo_target_error_component import (
        ApiV1AlertroutersIngestCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_target_availability_error_component import (
        ApiV1AlertroutersIngestCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_tolerations_error_component import (
        ApiV1AlertroutersIngestCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_ingest_create_workspace_id_error_component import (
        ApiV1AlertroutersIngestCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertroutersIngestCreateValidationError")


@_attrs_define
class ApiV1AlertroutersIngestCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertroutersIngestCreateAnnotationsErrorComponent |
            ApiV1AlertroutersIngestCreateArchivedAtErrorComponent | ApiV1AlertroutersIngestCreateArchivedErrorComponent |
            ApiV1AlertroutersIngestCreateArchivedReasonErrorComponent |
            ApiV1AlertroutersIngestCreateCriticalityErrorComponent | ApiV1AlertroutersIngestCreateDebugModeErrorComponent |
            ApiV1AlertroutersIngestCreateDisplayNameErrorComponent | ApiV1AlertroutersIngestCreateKindErrorComponent |
            ApiV1AlertroutersIngestCreateLabelClusterErrorComponent |
            ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponent |
            ApiV1AlertroutersIngestCreateLabelNamespaceErrorComponent |
            ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponent |
            ApiV1AlertroutersIngestCreateLabelPodErrorComponent | ApiV1AlertroutersIngestCreateLabelsErrorComponent |
            ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponent | ApiV1AlertroutersIngestCreateNameErrorComponent |
            ApiV1AlertroutersIngestCreateNonFieldErrorsErrorComponent |
            ApiV1AlertroutersIngestCreateOrganizationIdErrorComponent |
            ApiV1AlertroutersIngestCreatePlatformServiceErrorComponent | ApiV1AlertroutersIngestCreateProviderErrorComponent
            | ApiV1AlertroutersIngestCreateProviderIdErrorComponent |
            ApiV1AlertroutersIngestCreateProviderReferenceErrorComponent |
            ApiV1AlertroutersIngestCreateReconciliationEnabledErrorComponent |
            ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponent |
            ApiV1AlertroutersIngestCreateSlaTargetErrorComponent |
            ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponent |
            ApiV1AlertroutersIngestCreateSloTargetErrorComponent |
            ApiV1AlertroutersIngestCreateTargetAvailabilityErrorComponent |
            ApiV1AlertroutersIngestCreateTolerationsErrorComponent |
            ApiV1AlertroutersIngestCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertroutersIngestCreateAnnotationsErrorComponent
        | ApiV1AlertroutersIngestCreateArchivedAtErrorComponent
        | ApiV1AlertroutersIngestCreateArchivedErrorComponent
        | ApiV1AlertroutersIngestCreateArchivedReasonErrorComponent
        | ApiV1AlertroutersIngestCreateCriticalityErrorComponent
        | ApiV1AlertroutersIngestCreateDebugModeErrorComponent
        | ApiV1AlertroutersIngestCreateDisplayNameErrorComponent
        | ApiV1AlertroutersIngestCreateKindErrorComponent
        | ApiV1AlertroutersIngestCreateLabelClusterErrorComponent
        | ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponent
        | ApiV1AlertroutersIngestCreateLabelNamespaceErrorComponent
        | ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponent
        | ApiV1AlertroutersIngestCreateLabelPodErrorComponent
        | ApiV1AlertroutersIngestCreateLabelsErrorComponent
        | ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponent
        | ApiV1AlertroutersIngestCreateNameErrorComponent
        | ApiV1AlertroutersIngestCreateNonFieldErrorsErrorComponent
        | ApiV1AlertroutersIngestCreateOrganizationIdErrorComponent
        | ApiV1AlertroutersIngestCreatePlatformServiceErrorComponent
        | ApiV1AlertroutersIngestCreateProviderErrorComponent
        | ApiV1AlertroutersIngestCreateProviderIdErrorComponent
        | ApiV1AlertroutersIngestCreateProviderReferenceErrorComponent
        | ApiV1AlertroutersIngestCreateReconciliationEnabledErrorComponent
        | ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponent
        | ApiV1AlertroutersIngestCreateSlaTargetErrorComponent
        | ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponent
        | ApiV1AlertroutersIngestCreateSloTargetErrorComponent
        | ApiV1AlertroutersIngestCreateTargetAvailabilityErrorComponent
        | ApiV1AlertroutersIngestCreateTolerationsErrorComponent
        | ApiV1AlertroutersIngestCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertrouters_ingest_create_annotations_error_component import (
            ApiV1AlertroutersIngestCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_archived_at_error_component import (
            ApiV1AlertroutersIngestCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_archived_error_component import (
            ApiV1AlertroutersIngestCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_archived_reason_error_component import (
            ApiV1AlertroutersIngestCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_criticality_error_component import (
            ApiV1AlertroutersIngestCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_debug_mode_error_component import (
            ApiV1AlertroutersIngestCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_display_name_error_component import (
            ApiV1AlertroutersIngestCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_kind_error_component import (
            ApiV1AlertroutersIngestCreateKindErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_cluster_error_component import (
            ApiV1AlertroutersIngestCreateLabelClusterErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_namespace_error_component import (
            ApiV1AlertroutersIngestCreateLabelNamespaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_organization_error_component import (
            ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_pod_error_component import (
            ApiV1AlertroutersIngestCreateLabelPodErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_workspace_error_component import (
            ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_labels_error_component import (
            ApiV1AlertroutersIngestCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_name_error_component import (
            ApiV1AlertroutersIngestCreateNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_non_field_errors_error_component import (
            ApiV1AlertroutersIngestCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_organization_id_error_component import (
            ApiV1AlertroutersIngestCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_platform_service_error_component import (
            ApiV1AlertroutersIngestCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_provider_error_component import (
            ApiV1AlertroutersIngestCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_provider_id_error_component import (
            ApiV1AlertroutersIngestCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_provider_reference_error_component import (
            ApiV1AlertroutersIngestCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_reconciliation_enabled_error_component import (
            ApiV1AlertroutersIngestCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_sla_availability_error_component import (
            ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_sla_target_error_component import (
            ApiV1AlertroutersIngestCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_slo_availability_error_component import (
            ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_slo_target_error_component import (
            ApiV1AlertroutersIngestCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_target_availability_error_component import (
            ApiV1AlertroutersIngestCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_tolerations_error_component import (
            ApiV1AlertroutersIngestCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_workspace_id_error_component import (
            ApiV1AlertroutersIngestCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertroutersIngestCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateLabelClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateLabelPodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersIngestCreateLabelNamespaceErrorComponent):
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
        from ..models.api_v1_alertrouters_ingest_create_annotations_error_component import (
            ApiV1AlertroutersIngestCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_archived_at_error_component import (
            ApiV1AlertroutersIngestCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_archived_error_component import (
            ApiV1AlertroutersIngestCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_archived_reason_error_component import (
            ApiV1AlertroutersIngestCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_criticality_error_component import (
            ApiV1AlertroutersIngestCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_debug_mode_error_component import (
            ApiV1AlertroutersIngestCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_display_name_error_component import (
            ApiV1AlertroutersIngestCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_kind_error_component import (
            ApiV1AlertroutersIngestCreateKindErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_cluster_error_component import (
            ApiV1AlertroutersIngestCreateLabelClusterErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_criticality_error_component import (
            ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_namespace_error_component import (
            ApiV1AlertroutersIngestCreateLabelNamespaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_organization_error_component import (
            ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_pod_error_component import (
            ApiV1AlertroutersIngestCreateLabelPodErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_label_workspace_error_component import (
            ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_labels_error_component import (
            ApiV1AlertroutersIngestCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_name_error_component import (
            ApiV1AlertroutersIngestCreateNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_non_field_errors_error_component import (
            ApiV1AlertroutersIngestCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_organization_id_error_component import (
            ApiV1AlertroutersIngestCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_platform_service_error_component import (
            ApiV1AlertroutersIngestCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_provider_error_component import (
            ApiV1AlertroutersIngestCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_provider_id_error_component import (
            ApiV1AlertroutersIngestCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_provider_reference_error_component import (
            ApiV1AlertroutersIngestCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_reconciliation_enabled_error_component import (
            ApiV1AlertroutersIngestCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_sla_availability_error_component import (
            ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_sla_target_error_component import (
            ApiV1AlertroutersIngestCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_slo_availability_error_component import (
            ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_slo_target_error_component import (
            ApiV1AlertroutersIngestCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_target_availability_error_component import (
            ApiV1AlertroutersIngestCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_tolerations_error_component import (
            ApiV1AlertroutersIngestCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_ingest_create_workspace_id_error_component import (
            ApiV1AlertroutersIngestCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertroutersIngestCreateAnnotationsErrorComponent
                | ApiV1AlertroutersIngestCreateArchivedAtErrorComponent
                | ApiV1AlertroutersIngestCreateArchivedErrorComponent
                | ApiV1AlertroutersIngestCreateArchivedReasonErrorComponent
                | ApiV1AlertroutersIngestCreateCriticalityErrorComponent
                | ApiV1AlertroutersIngestCreateDebugModeErrorComponent
                | ApiV1AlertroutersIngestCreateDisplayNameErrorComponent
                | ApiV1AlertroutersIngestCreateKindErrorComponent
                | ApiV1AlertroutersIngestCreateLabelClusterErrorComponent
                | ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponent
                | ApiV1AlertroutersIngestCreateLabelNamespaceErrorComponent
                | ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponent
                | ApiV1AlertroutersIngestCreateLabelPodErrorComponent
                | ApiV1AlertroutersIngestCreateLabelsErrorComponent
                | ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponent
                | ApiV1AlertroutersIngestCreateNameErrorComponent
                | ApiV1AlertroutersIngestCreateNonFieldErrorsErrorComponent
                | ApiV1AlertroutersIngestCreateOrganizationIdErrorComponent
                | ApiV1AlertroutersIngestCreatePlatformServiceErrorComponent
                | ApiV1AlertroutersIngestCreateProviderErrorComponent
                | ApiV1AlertroutersIngestCreateProviderIdErrorComponent
                | ApiV1AlertroutersIngestCreateProviderReferenceErrorComponent
                | ApiV1AlertroutersIngestCreateReconciliationEnabledErrorComponent
                | ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponent
                | ApiV1AlertroutersIngestCreateSlaTargetErrorComponent
                | ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponent
                | ApiV1AlertroutersIngestCreateSloTargetErrorComponent
                | ApiV1AlertroutersIngestCreateTargetAvailabilityErrorComponent
                | ApiV1AlertroutersIngestCreateTolerationsErrorComponent
                | ApiV1AlertroutersIngestCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_0 = (
                        ApiV1AlertroutersIngestCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_1 = (
                        ApiV1AlertroutersIngestCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_2 = (
                        ApiV1AlertroutersIngestCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_3 = (
                        ApiV1AlertroutersIngestCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_4 = (
                        ApiV1AlertroutersIngestCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_5 = (
                        ApiV1AlertroutersIngestCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_6 = (
                        ApiV1AlertroutersIngestCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_7 = (
                        ApiV1AlertroutersIngestCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_8 = (
                        ApiV1AlertroutersIngestCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_9 = (
                        ApiV1AlertroutersIngestCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_10 = (
                        ApiV1AlertroutersIngestCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_11 = (
                        ApiV1AlertroutersIngestCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_12 = (
                        ApiV1AlertroutersIngestCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_13 = (
                        ApiV1AlertroutersIngestCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_14 = (
                        ApiV1AlertroutersIngestCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_15 = (
                        ApiV1AlertroutersIngestCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_16 = (
                        ApiV1AlertroutersIngestCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_17 = (
                        ApiV1AlertroutersIngestCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_18 = (
                        ApiV1AlertroutersIngestCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_19 = (
                        ApiV1AlertroutersIngestCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_20 = (
                        ApiV1AlertroutersIngestCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_21 = (
                        ApiV1AlertroutersIngestCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_22 = (
                        ApiV1AlertroutersIngestCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_23 = (
                        ApiV1AlertroutersIngestCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_24 = (
                        ApiV1AlertroutersIngestCreateLabelWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_25 = (
                        ApiV1AlertroutersIngestCreateLabelOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_26 = (
                        ApiV1AlertroutersIngestCreateLabelClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_27 = (
                        ApiV1AlertroutersIngestCreateLabelPodErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_ingest_create_error_type_28 = (
                        ApiV1AlertroutersIngestCreateLabelNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_ingest_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertrouters_ingest_create_error_type_29 = (
                    ApiV1AlertroutersIngestCreateLabelCriticalityErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertrouters_ingest_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertrouters_ingest_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertrouters_ingest_create_validation_error.additional_properties = d
        return api_v1_alertrouters_ingest_create_validation_error

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
