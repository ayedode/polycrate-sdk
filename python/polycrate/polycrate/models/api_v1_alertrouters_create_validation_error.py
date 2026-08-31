from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_alertrouters_create_annotations_error_component import (
        ApiV1AlertroutersCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_archived_at_error_component import (
        ApiV1AlertroutersCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_archived_error_component import (
        ApiV1AlertroutersCreateArchivedErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_archived_reason_error_component import (
        ApiV1AlertroutersCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_criticality_error_component import (
        ApiV1AlertroutersCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_debug_mode_error_component import (
        ApiV1AlertroutersCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_display_name_error_component import (
        ApiV1AlertroutersCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_kind_error_component import ApiV1AlertroutersCreateKindErrorComponent
    from ..models.api_v1_alertrouters_create_label_cluster_error_component import (
        ApiV1AlertroutersCreateLabelClusterErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_label_criticality_error_component import (
        ApiV1AlertroutersCreateLabelCriticalityErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_label_namespace_error_component import (
        ApiV1AlertroutersCreateLabelNamespaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_label_organization_error_component import (
        ApiV1AlertroutersCreateLabelOrganizationErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_label_pod_error_component import (
        ApiV1AlertroutersCreateLabelPodErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_label_workspace_error_component import (
        ApiV1AlertroutersCreateLabelWorkspaceErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_labels_error_component import ApiV1AlertroutersCreateLabelsErrorComponent
    from ..models.api_v1_alertrouters_create_name_error_component import ApiV1AlertroutersCreateNameErrorComponent
    from ..models.api_v1_alertrouters_create_non_field_errors_error_component import (
        ApiV1AlertroutersCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_organization_id_error_component import (
        ApiV1AlertroutersCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_platform_service_error_component import (
        ApiV1AlertroutersCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_provider_error_component import (
        ApiV1AlertroutersCreateProviderErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_provider_id_error_component import (
        ApiV1AlertroutersCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_provider_reference_error_component import (
        ApiV1AlertroutersCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_reconciliation_enabled_error_component import (
        ApiV1AlertroutersCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_sla_availability_error_component import (
        ApiV1AlertroutersCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_sla_target_error_component import (
        ApiV1AlertroutersCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_slo_availability_error_component import (
        ApiV1AlertroutersCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_slo_target_error_component import (
        ApiV1AlertroutersCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_target_availability_error_component import (
        ApiV1AlertroutersCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_tolerations_error_component import (
        ApiV1AlertroutersCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_alertrouters_create_workspace_id_error_component import (
        ApiV1AlertroutersCreateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1AlertroutersCreateValidationError")


@_attrs_define
class ApiV1AlertroutersCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1AlertroutersCreateAnnotationsErrorComponent | ApiV1AlertroutersCreateArchivedAtErrorComponent
            | ApiV1AlertroutersCreateArchivedErrorComponent | ApiV1AlertroutersCreateArchivedReasonErrorComponent |
            ApiV1AlertroutersCreateCriticalityErrorComponent | ApiV1AlertroutersCreateDebugModeErrorComponent |
            ApiV1AlertroutersCreateDisplayNameErrorComponent | ApiV1AlertroutersCreateKindErrorComponent |
            ApiV1AlertroutersCreateLabelClusterErrorComponent | ApiV1AlertroutersCreateLabelCriticalityErrorComponent |
            ApiV1AlertroutersCreateLabelNamespaceErrorComponent | ApiV1AlertroutersCreateLabelOrganizationErrorComponent |
            ApiV1AlertroutersCreateLabelPodErrorComponent | ApiV1AlertroutersCreateLabelsErrorComponent |
            ApiV1AlertroutersCreateLabelWorkspaceErrorComponent | ApiV1AlertroutersCreateNameErrorComponent |
            ApiV1AlertroutersCreateNonFieldErrorsErrorComponent | ApiV1AlertroutersCreateOrganizationIdErrorComponent |
            ApiV1AlertroutersCreatePlatformServiceErrorComponent | ApiV1AlertroutersCreateProviderErrorComponent |
            ApiV1AlertroutersCreateProviderIdErrorComponent | ApiV1AlertroutersCreateProviderReferenceErrorComponent |
            ApiV1AlertroutersCreateReconciliationEnabledErrorComponent |
            ApiV1AlertroutersCreateSlaAvailabilityErrorComponent | ApiV1AlertroutersCreateSlaTargetErrorComponent |
            ApiV1AlertroutersCreateSloAvailabilityErrorComponent | ApiV1AlertroutersCreateSloTargetErrorComponent |
            ApiV1AlertroutersCreateTargetAvailabilityErrorComponent | ApiV1AlertroutersCreateTolerationsErrorComponent |
            ApiV1AlertroutersCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1AlertroutersCreateAnnotationsErrorComponent
        | ApiV1AlertroutersCreateArchivedAtErrorComponent
        | ApiV1AlertroutersCreateArchivedErrorComponent
        | ApiV1AlertroutersCreateArchivedReasonErrorComponent
        | ApiV1AlertroutersCreateCriticalityErrorComponent
        | ApiV1AlertroutersCreateDebugModeErrorComponent
        | ApiV1AlertroutersCreateDisplayNameErrorComponent
        | ApiV1AlertroutersCreateKindErrorComponent
        | ApiV1AlertroutersCreateLabelClusterErrorComponent
        | ApiV1AlertroutersCreateLabelCriticalityErrorComponent
        | ApiV1AlertroutersCreateLabelNamespaceErrorComponent
        | ApiV1AlertroutersCreateLabelOrganizationErrorComponent
        | ApiV1AlertroutersCreateLabelPodErrorComponent
        | ApiV1AlertroutersCreateLabelsErrorComponent
        | ApiV1AlertroutersCreateLabelWorkspaceErrorComponent
        | ApiV1AlertroutersCreateNameErrorComponent
        | ApiV1AlertroutersCreateNonFieldErrorsErrorComponent
        | ApiV1AlertroutersCreateOrganizationIdErrorComponent
        | ApiV1AlertroutersCreatePlatformServiceErrorComponent
        | ApiV1AlertroutersCreateProviderErrorComponent
        | ApiV1AlertroutersCreateProviderIdErrorComponent
        | ApiV1AlertroutersCreateProviderReferenceErrorComponent
        | ApiV1AlertroutersCreateReconciliationEnabledErrorComponent
        | ApiV1AlertroutersCreateSlaAvailabilityErrorComponent
        | ApiV1AlertroutersCreateSlaTargetErrorComponent
        | ApiV1AlertroutersCreateSloAvailabilityErrorComponent
        | ApiV1AlertroutersCreateSloTargetErrorComponent
        | ApiV1AlertroutersCreateTargetAvailabilityErrorComponent
        | ApiV1AlertroutersCreateTolerationsErrorComponent
        | ApiV1AlertroutersCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_alertrouters_create_annotations_error_component import (
            ApiV1AlertroutersCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_archived_at_error_component import (
            ApiV1AlertroutersCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_archived_error_component import (
            ApiV1AlertroutersCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_archived_reason_error_component import (
            ApiV1AlertroutersCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_criticality_error_component import (
            ApiV1AlertroutersCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_debug_mode_error_component import (
            ApiV1AlertroutersCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_display_name_error_component import (
            ApiV1AlertroutersCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_kind_error_component import ApiV1AlertroutersCreateKindErrorComponent
        from ..models.api_v1_alertrouters_create_label_cluster_error_component import (
            ApiV1AlertroutersCreateLabelClusterErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_label_namespace_error_component import (
            ApiV1AlertroutersCreateLabelNamespaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_label_organization_error_component import (
            ApiV1AlertroutersCreateLabelOrganizationErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_label_pod_error_component import (
            ApiV1AlertroutersCreateLabelPodErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_label_workspace_error_component import (
            ApiV1AlertroutersCreateLabelWorkspaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_labels_error_component import (
            ApiV1AlertroutersCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_name_error_component import ApiV1AlertroutersCreateNameErrorComponent
        from ..models.api_v1_alertrouters_create_non_field_errors_error_component import (
            ApiV1AlertroutersCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_organization_id_error_component import (
            ApiV1AlertroutersCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_platform_service_error_component import (
            ApiV1AlertroutersCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_provider_error_component import (
            ApiV1AlertroutersCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_provider_id_error_component import (
            ApiV1AlertroutersCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_provider_reference_error_component import (
            ApiV1AlertroutersCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_reconciliation_enabled_error_component import (
            ApiV1AlertroutersCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_sla_availability_error_component import (
            ApiV1AlertroutersCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_sla_target_error_component import (
            ApiV1AlertroutersCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_slo_availability_error_component import (
            ApiV1AlertroutersCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_slo_target_error_component import (
            ApiV1AlertroutersCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_target_availability_error_component import (
            ApiV1AlertroutersCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_tolerations_error_component import (
            ApiV1AlertroutersCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_workspace_id_error_component import (
            ApiV1AlertroutersCreateWorkspaceIdErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1AlertroutersCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateLabelWorkspaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateLabelOrganizationErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateLabelClusterErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateLabelPodErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1AlertroutersCreateLabelNamespaceErrorComponent):
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
        from ..models.api_v1_alertrouters_create_annotations_error_component import (
            ApiV1AlertroutersCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_archived_at_error_component import (
            ApiV1AlertroutersCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_archived_error_component import (
            ApiV1AlertroutersCreateArchivedErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_archived_reason_error_component import (
            ApiV1AlertroutersCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_criticality_error_component import (
            ApiV1AlertroutersCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_debug_mode_error_component import (
            ApiV1AlertroutersCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_display_name_error_component import (
            ApiV1AlertroutersCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_kind_error_component import ApiV1AlertroutersCreateKindErrorComponent
        from ..models.api_v1_alertrouters_create_label_cluster_error_component import (
            ApiV1AlertroutersCreateLabelClusterErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_label_criticality_error_component import (
            ApiV1AlertroutersCreateLabelCriticalityErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_label_namespace_error_component import (
            ApiV1AlertroutersCreateLabelNamespaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_label_organization_error_component import (
            ApiV1AlertroutersCreateLabelOrganizationErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_label_pod_error_component import (
            ApiV1AlertroutersCreateLabelPodErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_label_workspace_error_component import (
            ApiV1AlertroutersCreateLabelWorkspaceErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_labels_error_component import (
            ApiV1AlertroutersCreateLabelsErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_name_error_component import ApiV1AlertroutersCreateNameErrorComponent
        from ..models.api_v1_alertrouters_create_non_field_errors_error_component import (
            ApiV1AlertroutersCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_organization_id_error_component import (
            ApiV1AlertroutersCreateOrganizationIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_platform_service_error_component import (
            ApiV1AlertroutersCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_provider_error_component import (
            ApiV1AlertroutersCreateProviderErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_provider_id_error_component import (
            ApiV1AlertroutersCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_provider_reference_error_component import (
            ApiV1AlertroutersCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_reconciliation_enabled_error_component import (
            ApiV1AlertroutersCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_sla_availability_error_component import (
            ApiV1AlertroutersCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_sla_target_error_component import (
            ApiV1AlertroutersCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_slo_availability_error_component import (
            ApiV1AlertroutersCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_slo_target_error_component import (
            ApiV1AlertroutersCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_target_availability_error_component import (
            ApiV1AlertroutersCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_tolerations_error_component import (
            ApiV1AlertroutersCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_alertrouters_create_workspace_id_error_component import (
            ApiV1AlertroutersCreateWorkspaceIdErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1AlertroutersCreateAnnotationsErrorComponent
                | ApiV1AlertroutersCreateArchivedAtErrorComponent
                | ApiV1AlertroutersCreateArchivedErrorComponent
                | ApiV1AlertroutersCreateArchivedReasonErrorComponent
                | ApiV1AlertroutersCreateCriticalityErrorComponent
                | ApiV1AlertroutersCreateDebugModeErrorComponent
                | ApiV1AlertroutersCreateDisplayNameErrorComponent
                | ApiV1AlertroutersCreateKindErrorComponent
                | ApiV1AlertroutersCreateLabelClusterErrorComponent
                | ApiV1AlertroutersCreateLabelCriticalityErrorComponent
                | ApiV1AlertroutersCreateLabelNamespaceErrorComponent
                | ApiV1AlertroutersCreateLabelOrganizationErrorComponent
                | ApiV1AlertroutersCreateLabelPodErrorComponent
                | ApiV1AlertroutersCreateLabelsErrorComponent
                | ApiV1AlertroutersCreateLabelWorkspaceErrorComponent
                | ApiV1AlertroutersCreateNameErrorComponent
                | ApiV1AlertroutersCreateNonFieldErrorsErrorComponent
                | ApiV1AlertroutersCreateOrganizationIdErrorComponent
                | ApiV1AlertroutersCreatePlatformServiceErrorComponent
                | ApiV1AlertroutersCreateProviderErrorComponent
                | ApiV1AlertroutersCreateProviderIdErrorComponent
                | ApiV1AlertroutersCreateProviderReferenceErrorComponent
                | ApiV1AlertroutersCreateReconciliationEnabledErrorComponent
                | ApiV1AlertroutersCreateSlaAvailabilityErrorComponent
                | ApiV1AlertroutersCreateSlaTargetErrorComponent
                | ApiV1AlertroutersCreateSloAvailabilityErrorComponent
                | ApiV1AlertroutersCreateSloTargetErrorComponent
                | ApiV1AlertroutersCreateTargetAvailabilityErrorComponent
                | ApiV1AlertroutersCreateTolerationsErrorComponent
                | ApiV1AlertroutersCreateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_0 = (
                        ApiV1AlertroutersCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_1 = (
                        ApiV1AlertroutersCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_2 = (
                        ApiV1AlertroutersCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_3 = (
                        ApiV1AlertroutersCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_4 = (
                        ApiV1AlertroutersCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_5 = (
                        ApiV1AlertroutersCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_6 = (
                        ApiV1AlertroutersCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_7 = (
                        ApiV1AlertroutersCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_8 = (
                        ApiV1AlertroutersCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_9 = (
                        ApiV1AlertroutersCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_10 = (
                        ApiV1AlertroutersCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_11 = (
                        ApiV1AlertroutersCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_12 = (
                        ApiV1AlertroutersCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_13 = (
                        ApiV1AlertroutersCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_14 = (
                        ApiV1AlertroutersCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_15 = (
                        ApiV1AlertroutersCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_16 = (
                        ApiV1AlertroutersCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_17 = (
                        ApiV1AlertroutersCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_18 = (
                        ApiV1AlertroutersCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_19 = (
                        ApiV1AlertroutersCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_20 = (
                        ApiV1AlertroutersCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_21 = (
                        ApiV1AlertroutersCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_22 = (
                        ApiV1AlertroutersCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_23 = (
                        ApiV1AlertroutersCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_24 = (
                        ApiV1AlertroutersCreateLabelWorkspaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_25 = (
                        ApiV1AlertroutersCreateLabelOrganizationErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_26 = (
                        ApiV1AlertroutersCreateLabelClusterErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_27 = (
                        ApiV1AlertroutersCreateLabelPodErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_alertrouters_create_error_type_28 = (
                        ApiV1AlertroutersCreateLabelNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_alertrouters_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_alertrouters_create_error_type_29 = (
                    ApiV1AlertroutersCreateLabelCriticalityErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_alertrouters_create_error_type_29

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_alertrouters_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_alertrouters_create_validation_error.additional_properties = d
        return api_v1_alertrouters_create_validation_error

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
